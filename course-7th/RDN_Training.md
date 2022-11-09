### 1. 选用超分网络

* [Residual Dense Network for Image Super-Resolution.](https://arxiv.org/abs/1802.08797)
* [DECA: Learning an Animatable Detailed 3D Face Model from In-The-Wild Images(SIGGRAPH 2021).](https://github.com/YadiraF/DECA)

#### 1.1 The architecture of theresidual dense network (RDN)
![[1667958614802.png]]
$\quad \quad$ ![[1667958666969.png]]

### 2. 训练
![[RDN_training.png]]

### 3. Results
共训练50代，Best Epoch 为45，其峰值信噪比为37.69
测试结果如下：
![[Pasted image 20221109100658.png]]
左侧为低分辨率数据，右侧为测试表现























































