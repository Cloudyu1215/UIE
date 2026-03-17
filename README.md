<p align="center">
<img src="Figs\0.png" width="100%">
</p>


[![arXiv](https://img.shields.io/badge/arXiv-Paper-red.svg)](https://github.com/Cloudyu1215/UIE)
------
Official implementation of  
**"Advancing Visual Reliability: Color-Accurate Underwater Image Enhancement for Real-Time Underwater Missions"**.

<p align="center">
<img src="Figs\all_compare.gif" width="80%">
</p>

<br>
<br>

# 🔥 Highlights

- **Ultra-lightweight model**
  - Only **3.88K parameters**
  - **0.145 GFLOPs**
- **Real-time performance**
  - **409 FPS on GPU**
  - **30 FPS on NVIDIA Jetson Orin NX**
- **Strong enhancement capability**
  - Superior performance on **8 underwater datasets**
  - **29.7% improvement in UCIQE** under real underwater conditions
- **Practical deployment**
  - Successfully deployed on **ROV platform**
  - Improves **downstream instance segmentation performance**

<br>
<br>

## 🧠 Method
### Overall Framework

<p align="center">
  <img src="Figs/Pipeline.png" width="900">
</p>

### MRDConv
<p align="center">
  <img src="Figs/MRDConv.png" height="500">
</p>


<br>
<br>

# 📷 Visual Results


- [Intermediate Process Visualization](Figs/02_vis.pdf)
- [Visual Result 01](Figs/06_compare1.pdf)
- [Visual Result 02](Figs/07_compare2.pdf)
- [Visual Result 03](Figs/08_compare3.pdf)
- [Ablation Study 01](Figs/03_ab1.pdf)
- [Ablation Study 02](Figs/04_ab2.pdf)
- [Ablation Study 03](Figs/05_ab3.pdf)
- [Instance Segmentation](Figs/11_UIIS.pdf)



Our method produces:

- more natural colors
- clearer textures
- stable contrast across different underwater scenes

<br>
<br>

# 🌊 Real-world Deployment

We conducted experiments in:

- **Controlled water tank**
  - [Underwater Camera](Figs/09_camera.pdf)

  - [Downstream Task](Figs/12_seg.pdf)

- **Qiandao Lake ROV platform**
  <p align="center">
  <img src="Figs\Atlas.png" width="80%">
  </p>

  
  - [Rov Deployment](Figs/10_rov.pdf)

  

Results show significant improvements in:

- visibility
- feature extraction
- feature matching stability

<br>
<br>

# 📦 Datasets

Experiments are conducted on the following datasets:

| Dataset | Images | Link |
| ------- | ------ |------|
| UIEB    | 890    |[UIEB](https://arxiv.org/pdf/1901.05495.pdf)|
| LSUI    | 4,279  |[LSUI](https://arxiv.org/pdf/2111.11843)|
| EUVP-D  | 2,185  |[EUVP-D](https://ieeexplore.ieee.org/document/9001231)|
| EUVP-I  | 5,500  |[EUVP-I](https://ieeexplore.ieee.org/document/9001231)|
| EUVP-S  | 3,700  |[EUVP-S](https://ieeexplore.ieee.org/document/9001231)|

Additional generalization tests:
- [U45](https://arxiv.org/abs/1906.06819) 
- [RUIE](https://arxiv.org/abs/1901.05320)
- [ColorCheck7](https://github.com/kaibopiggy/two-No-reference-image-dataset/tree/main/Color-Check7)
- [UIIS](https://github.com/LiamLian0727/WaterMask)




<br>
<br>




# 🙏 Acknowledgement

This work was supported by:

- **Institute of Artificial Intelligence (TeleAI), China Telecom, P. R. China**

<br>
<br>

# 📄 Citiation

If you find this work useful, please cite:

```bibtex
@article{UIIS10K_Dataset_2025,
    author    = {Hua Li, Shijie Lian, Zhiyuan Li, Runmin Cong, Chongyi Li},
    title     = {Taming SAM for Underwater Instance Segmentation and Beyond},
    year      = {2025},
    journal   = {arXiv preprint arXiv:2505.15581},
}