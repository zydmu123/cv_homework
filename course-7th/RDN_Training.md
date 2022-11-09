### 1. 选用超分网络

* [Residual Dense Network for Image Super-Resolution.](https://arxiv.org/abs/1802.08797)


#### 1.1 The architecture of theresidual dense network (RDN)
![1667960324531](https://user-images.githubusercontent.com/111970347/200721110-5800bcf7-3407-4f27-80f2-fdc303daeec7.png)
$\quad \quad$ ![image](https://user-images.githubusercontent.com/111970347/200721170-f37393a3-74ae-41a5-94af-293c3e5a985a.png)

### 2. 训练
![RDN_training](https://user-images.githubusercontent.com/111970347/200721219-b6c63540-702a-4e52-852d-ba84568613a7.png)



### 3. Results
共训练50代，Best Epoch 为45，其峰值信噪比为37.69 \
测试结果如下：
![1667960426115](https://user-images.githubusercontent.com/111970347/200721331-5d26e94f-bbcf-4308-b3bd-74fadf38d88a.png)

左侧为低分辨率数据，右侧为测试表现























































