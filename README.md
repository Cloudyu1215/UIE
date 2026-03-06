# Color Back, Model Light

### An Efficient Framework for Real-Time Underwater Image Enhancement





Official implementation of **"Color Back, Model Light: An Efficient Framework for Real-Time Underwater Image Enhancement and Beyond"**.

This work proposes an **extremely lightweight underwater image enhancement framework** designed for **real-time underwater vision systems**, achieving **state-of-the-art performance with only 3.55K parameters and 409 FPS inference speed**.

The proposed framework focuses on **color restoration efficiency**, making it suitable for **embedded underwater platforms such as ROVs and AUVs**.

------

# 🔥 Highlights

- **Ultra-lightweight model**
  - Only **3.55K parameters**
  - **0.184 GFLOPs**
- **Real-time performance**
  - **409 FPS on GPU**
  - **25 FPS on NVIDIA Jetson Orin NX**
- **Strong enhancement capability**
  - SOTA performance on **9 underwater datasets**
  - **29.7% improvement in UCIQE** under real underwater conditions
- **Practical deployment**
  - Successfully deployed on **ROV platform**
  - Improves **downstream instance segmentation performance**

------

# 🧠 Framework Overview

Our method consists of three main components:

### 1️⃣ Adaptive Weighted Channel Compensation (AWCC)

- Uses **green channel as reference anchor**
- Dynamically compensates **red and blue channels**
- Learns adaptive weights for different underwater environments

### 2️⃣ Multi-branch Re-parameterized Dilated Convolution (MRDConv)

- Multi-branch dilated convolution during training
- Re-parameterized into **single convolution during inference**
- Provides **large receptive field with minimal cost**

### 3️⃣ Statistical Global Color Adjustment (SGCA)

- Extracts **global statistical priors**
- Predicts
  - temperature shift
  - tint shift
  - saturation gain
- Achieves efficient global color correction

------

# 📊 Performance

| Method      | Params    | FLOPs      | FPS     | PSNR      | SSIM      |
| ----------- | --------- | ---------- | ------- | --------- | --------- |
| MobileIE    | 4.0K      | 0.146G     | 678     | 22.84     | 0.894     |
| PhaseFormer | 1.7M      | 13.04G     | 45      | 23.47     | 0.842     |
| **Ours**    | **3.55K** | **0.184G** | **409** | **24.33** | **0.902** |

Our model achieves the **best trade-off between efficiency and enhancement quality**.

------

# 📷 Visual Results





Our method produces:

- more natural colors
- clearer textures
- stable contrast across different underwater scenes

------

# 📦 Datasets

Experiments are conducted on the following datasets:

| Dataset | Images |
| ------- | ------ |
| UIEB    | 890    |
| LSUI    | 4,279  |
| EUVP-D  | 2,185  |
| EUVP-I  | 5,500  |
| EUVP-S  | 3,700  |

Additional generalization tests:

- U45
- RUIE
- ColorChecker7

------

# ⚙️ Installation

```
git clone https://github.com/yourname/color-back-model-light.git

cd color-back-model-light

conda create -n uie python=3.9
conda activate uie

pip install -r requirements.txt
```

------

# 🚀 Training

```
python train.py \
    --dataset UIEB \
    --batch_size 8 \
    --lr 2e-4 \
    --epochs 400
```

------

# 🔍 Inference

```
python inference.py \
    --input_dir ./test_images \
    --output_dir ./results \
    --weights checkpoints/model.pth
```

------

# 🖥 Deployment (TensorRT)

The model can be deployed on **edge devices such as NVIDIA Jetson Orin NX**.

Example workflow:

```
python export_onnx.py

trtexec --onnx=model.onnx --fp16
```

Deployment performance:

| Device         | Resolution | FPS  |
| -------------- | ---------- | ---- |
| RTX A100       | 640×480    | 409  |
| Jetson Orin NX | 640×480    | 25   |

------

# 📈 Downstream Task Improvement

Enhanced images improve **underwater instance segmentation performance** on the **UIIS dataset**.

| Method    | mAP       |
| --------- | --------- |
| WaterMask | 0.225     |
| FiveA+    | 0.234     |
| MobileIE  | 0.231     |
| **Ours**  | **0.237** |

------

# 🌊 Real-world Deployment

We conducted experiments in:

- **Controlled water tank**
- **Qiandao Lake ROV platform**

Results show significant improvements in:

- visibility
- feature extraction
- feature matching stability

------

# 📄 Paper

If you find this work useful, please cite:

```
@article{zhou2026colorback,
  title={Color Back, Model Light: An Efficient Framework for Real-Time Underwater Image Enhancement and Beyond},
  author={Zhou, Yiqiang and Sun, Zhe and Lu, Jijun and Zheng, Ye and Chen, Yifan and Li, Xuelong},
  journal={IEEE},
  year={2026}
}
```

------

# 🙏 Acknowledgement

This work was supported by:

- **China Telecom TeleAI**
- **Northwestern Polytechnical University**
- **Fudan University**

------

# 📬 Contact

If you have questions, feel free to contact:

**Yiqiang Zhou**

Email:

```
cloudyu1215@outlook.com
```

------

⭐ If this project helps your research, please give it a **star**!