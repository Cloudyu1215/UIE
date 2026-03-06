# Color Back, Model Light

### An Efficient Framework for Real-Time Underwater Image Enhancement



<iframe frameborder="0" class="juxtapose" width="480" height="360" src="https://cdn.knightlab.com/libs/juxtapose/latest/embed/index.html?uid=c5f56a66-18fe-11f1-ba1b-0e6f42328d7d"></iframe>



Official implementation of **"Color Back, Model Light: An Efficient Framework for Real-Time Underwater Image Enhancement and Beyond"**.


------

# 🔥 Highlights

- **Ultra-lightweight model**
  - Only **3.55K parameters**
  - **0.184 GFLOPs**
- **Real-time performance**
  - **409 FPS on GPU**
  - **25 FPS on NVIDIA Jetson Orin NX**
- **Strong enhancement capability**
  - Superior performance on **9 underwater datasets**
  - **29.7% improvement in UCIQE** under real underwater conditions
- **Practical deployment**
  - Successfully deployed on **ROV platform**
  - Improves **downstream instance segmentation performance**

------

## 🧠 Method
## Framework

<p align="center">
  <img src="Figs/Pipeline.png" width="900">
</p>

## MRDConv
<p align="center">
  <img src="Figs/MRDConv.png" height="550">
</p>

# 📷 Visual Results


- [Internal_vis](Figs/02_vis.pdf)
- [Visual_1](Figs/06_compare1.pdf)
- [Visual_2](Figs/07_compare2.pdf)
- [Visual_3](Figs/08_compare3.pdf)
- [Ablation_1](Figs/03_ab1.pdf)
- [Ablation_2](Figs/04_ab2.pdf)
- [Ablation_3](Figs/05_ab3.pdf)
- [Instance seg](Figs/11_UIIS.pdf)




Our method produces:

- more natural colors
- clearer textures
- stable contrast across different underwater scenes

------

# 🌊 Real-world Deployment

We conducted experiments in:

- **Controlled water tank**
- **Qiandao Lake ROV platform**

- [Underwater camera](Figs/09_camera.pdf)
- [Rov](Figs/10_rov.pdf)
- [Camera seg](Figs/12_seg.pdf)
  

Results show significant improvements in:

- visibility
- feature extraction
- feature matching stability

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

[UIEB](https://arxiv.org/pdf/1901.05495.pdf)
[LSUI](https://arxiv.org/pdf/2111.11843)
[EUVP](https://ieeexplore.ieee.org/document/9001231)
[U45](https://arxiv.org/abs/1906.06819) 
[RUIE](https://arxiv.org/abs/1901.05320)



------

# 🙏 Acknowledgement

This work was supported by:

- **Institute of Artificial Intelligence (TeleAI), China Telecom**


------
# 📄 Paper

If you find this work useful, please cite: