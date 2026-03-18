import torch
import torch.nn as nn
class MRDConv(nn.Module):
    def __init__(self, in_channels, out_channels, rep_scale=4):
        super(MRDConv, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        
        mid_channels = out_channels * rep_scale

        self.branch_s3 = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=3, stride=1, padding=2, dilation=2, bias=False),
            nn.BatchNorm2d(mid_channels)
        )
        self.branch_s2 = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=2, stride=1, padding=1, dilation=2, bias=False),
            nn.BatchNorm2d(mid_channels)
        )
        self.branch_s1 = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(mid_channels)
        )
        self.branch_v = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=(3, 2), stride=1, padding=(2, 1), dilation=(2, 2), bias=False),
            nn.BatchNorm2d(mid_channels)
        )
        self.branch_h = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=(2, 3), stride=1, padding=(1, 2), dilation=(2, 2), bias=False),
            nn.BatchNorm2d(mid_channels)
        )

        self.fusion_conv = nn.Conv2d(mid_channels, out_channels, kernel_size=1, stride=1, padding=0)

    def forward(self, x):
        # B,mid_c,H,W
        x_s3 = self.branch_s3(x)
        x_s2 = self.branch_s2(x)
        x_s1 = self.branch_s1(x)
        x_v  = self.branch_v(x)
        x_h  = self.branch_h(x)
        
        x_sum = x_s3 + x_s2 + x_s1 + x_v + x_h
        x_final = self.fusion_conv(x_sum)
        print(x_final.shape)
        return x_final  #B,out_c,H,W

    def _fuse_bn(self, branch):

        conv = branch[0] 
        bn = branch[1]   
        
        w = conv.weight
        mean = bn.running_mean
        var_sqrt = torch.sqrt(bn.running_var + bn.eps)
        beta = bn.bias
        gamma = bn.weight
        
        if conv.bias is not None: #bias=True
            b = conv.bias
        else:
            b = mean.new_zeros(mean.shape) #bias=False
            
        w = w * (gamma / var_sqrt).view(-1, 1, 1, 1)
        b = (b - mean) * gamma / var_sqrt + beta
        return w, b

    def slim(self):

        w_fusion = self.fusion_conv.weight # out_c,mid_c,1,1
        # print(w_fusion.shape)
        b_fusion = self.fusion_conv.bias 
        # print(b_fusion.shape)
        
        oc_fusion, mid_c, _, _ = w_fusion.shape 
        ic_in = self.in_channels #==3

        def make_empty_5x5(device, dtype):
            return torch.zeros(mid_c, ic_in, 5, 5, device=device, dtype=dtype)

        w_s3, b_s3 = self._fuse_bn(self.branch_s3)
        k_s3 = make_empty_5x5(w_s3.device, w_s3.dtype)
        k_s3[:, :, 0::2, 0::2] = w_s3

        # Branch S2
        w_s2, b_s2 = self._fuse_bn(self.branch_s2)
        k_s2 = make_empty_5x5(w_s2.device, w_s2.dtype)
        k_s2[:, :, 1::2, 1::2] = w_s2
        
        # Branch S1
        w_s1, b_s1 = self._fuse_bn(self.branch_s1)
        k_s1 = make_empty_5x5(w_s1.device, w_s1.dtype)
        k_s1[:, :, 2, 2] = w_s1.squeeze() 
        
        # Branch V
        w_v, b_v = self._fuse_bn(self.branch_v)
        k_v = make_empty_5x5(w_v.device, w_v.dtype)
        k_v[:, :, 0::2, 1::2] = w_v
        
        # Branch H
        w_h, b_h = self._fuse_bn(self.branch_h)
        k_h = make_empty_5x5(w_h.device, w_h.dtype)
        k_h[:, :, 1::2, 0::2] = w_h
        print(k_h.shape)
        k_sum = k_s3 + k_s2 + k_s1 + k_v + k_h
        print(k_sum.shape)
        b_sum = b_s3 + b_s2 + b_s1 + b_v + b_h
        print(b_sum.shape)

        k_sum_flat = k_sum.view(mid_c, -1)  

 
        w_fusion_flat = w_fusion.view(self.out_channels, -1) 

        final_weight_flat = torch.matmul(w_fusion_flat, k_sum_flat) 

     
        final_weight = final_weight_flat.view(self.out_channels, ic_in, 5, 5)

        final_bias = torch.matmul(w_fusion_flat, b_sum)

        if b_fusion is not None:
            final_bias = final_bias + b_fusion
            
        return final_weight, final_bias


import torch
import matplotlib.pyplot as plt

import numpy as np


def kernel_to_map(W, mode="mean_abs"):
    """
    W: (out_c, in_c, kh, kw)
    return: (kh, kw) 2D map
    """
    if mode == "mean_abs":
        M = W.abs().mean(dim=(0, 1))
    elif mode == "l2":
        M = torch.sqrt((W ** 2).sum(dim=(0, 1)) + 1e-12)
    elif mode == "mean":
        M = W.mean(dim=(0, 1))
    else:
        raise ValueError("mode in {mean_abs, l2, mean}")
    return M.detach().cpu()



def show_map(M, title="", cmap="magma"):
    plt.figure(figsize=(3,3))
    cmap = plt.get_cmap("magma")
    vmin = 0
    vmax = torch.quantile(M, 1.0)
    new_cmap = cmap(np.linspace(0.1, 0.6, 256))  
    plt.imshow(torch.log1p(M), cmap=cmap, vmin=vmin, vmax=vmax)
    # plt.imshow(torch.log1p(M), cmap=plt.cm.colors.ListedColormap(new_cmap))
    # plt.imshow(M, cmap=cmap)
    plt.colorbar(fraction=0.046, pad=0.04)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

@torch.no_grad()
def visualize_mrdconv_weights(m: "MRDConv", mode="mean_abs"):
    m.eval()


    w_s3, b_s3 = m._fuse_bn(m.branch_s3)  # (mid, in, 3, 3)
    w_s2, b_s2 = m._fuse_bn(m.branch_s2)  # (mid, in, 2, 2)
    w_s1, b_s1 = m._fuse_bn(m.branch_s1)  # (mid, in, 1, 1)
    w_v,  b_v  = m._fuse_bn(m.branch_v)   # (mid, in, 3, 2)
    w_h,  b_h  = m._fuse_bn(m.branch_h)   # (mid, in, 2, 3)


    mid_c = w_s3.shape[0]
    ic_in = m.in_channels
    def empty_5x5(dev, dt): return torch.zeros(mid_c, ic_in, 5, 5, device=dev, dtype=dt)

    k_s3 = empty_5x5(w_s3.device, w_s3.dtype); k_s3[:, :, 0::2, 0::2] = w_s3
    k_s2 = empty_5x5(w_s2.device, w_s2.dtype); k_s2[:, :, 1::2, 1::2] = w_s2
    k_s1 = empty_5x5(w_s1.device, w_s1.dtype)/10; k_s1[:, :, 2, 2]       = w_s1.squeeze()
    k_v  = empty_5x5(w_v.device,  w_v.dtype ); k_v[:,  :, 0::2, 1::2] = w_v
    k_h  = empty_5x5(w_h.device,  w_h.dtype ); k_h[:,  :, 1::2, 0::2] = w_h


    show_map(kernel_to_map(k_s3, mode), f"Branch S3 embedded 5x5 ({mode})")
    show_map(kernel_to_map(k_s2, mode), f"Branch S2 embedded 5x5 ({mode})")
    show_map(kernel_to_map(k_s1, mode), f"Branch S1 embedded 5x5 ({mode})")
    show_map(kernel_to_map(k_v,  mode), f"Branch V  embedded 5x5 ({mode})")
    show_map(kernel_to_map(k_h,  mode), f"Branch H  embedded 5x5 ({mode})")


    k_sum = k_s3 + k_s2 + k_s1 + k_v + k_h
    show_map(kernel_to_map(k_sum, mode), f"Sum kernel in mid space 5x5 ({mode})")


    W_final, b_final = m.slim()
    show_map(kernel_to_map(W_final, mode), f"Final re-parameterized 5x5 ({mode})")



if __name__ == "__main__":


    in_channels = 3
    out_channels = 3
    rep_scale = 4

    model = MRDConv(in_channels, out_channels, rep_scale)
    visualize_mrdconv_weights(model, mode="mean_abs") 
    model.eval()  
    

    x = torch.randn(1, in_channels, 64, 64)


    with torch.no_grad():
        out_train = model(x)

    print("Forward output shape:", out_train.shape)


    W_final, b_final = model.slim()

    reparam_conv = nn.Conv2d(
        in_channels,
        out_channels,
        kernel_size=5,
        stride=1,
        padding=2,
        bias=True
    )

    reparam_conv.weight.data = W_final
    reparam_conv.bias.data = b_final

    reparam_conv.eval()


    with torch.no_grad():
        out_infer = reparam_conv(x)

    print("Reparam output shape:", out_infer.shape)


    diff = torch.abs(out_train - out_infer).mean()
    print("Mean difference:", diff.item())