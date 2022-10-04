<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#pip-install--i-https://pypi.tuna.tsinghua.edu.cn/simple-imageio-ffmpeg" data-toc-modified-id="pip-install--i-https://pypi.tuna.tsinghua.edu.cn/simple-imageio-ffmpeg-0.1"><span class="toc-item-num">0.1&nbsp;&nbsp;</span>pip install -i <a href="https://pypi.tuna.tsinghua.edu.cn/simple" rel="nofollow" target="_blank">https://pypi.tuna.tsinghua.edu.cn/simple</a> imageio-ffmpeg</a></span></li><li><span><a href="#pip-install--i-https://pypi.tuna.tsinghua.edu.cn/simple-imageio" data-toc-modified-id="pip-install--i-https://pypi.tuna.tsinghua.edu.cn/simple-imageio-0.2"><span class="toc-item-num">0.2&nbsp;&nbsp;</span>pip install -i <a href="https://pypi.tuna.tsinghua.edu.cn/simple" rel="nofollow" target="_blank">https://pypi.tuna.tsinghua.edu.cn/simple</a> imageio</a></span></li><li><span><a href="#利用opencv读取图片并显示" data-toc-modified-id="利用opencv读取图片并显示-0.3"><span class="toc-item-num">0.3&nbsp;&nbsp;</span>利用opencv读取图片并显示</a></span></li><li><span><a href="#RGB-&amp;-BGR" data-toc-modified-id="RGB-&amp;-BGR-0.4"><span class="toc-item-num">0.4&nbsp;&nbsp;</span>RGB &amp; BGR</a></span></li><li><span><a href="#图像保存-JPEG和PNG" data-toc-modified-id="图像保存-JPEG和PNG-0.5"><span class="toc-item-num">0.5&nbsp;&nbsp;</span>图像保存 JPEG和PNG</a></span></li><li><span><a href="#颜色空间转换" data-toc-modified-id="颜色空间转换-0.6"><span class="toc-item-num">0.6&nbsp;&nbsp;</span>颜色空间转换</a></span></li><li><span><a href="#RGB" data-toc-modified-id="RGB-0.7"><span class="toc-item-num">0.7&nbsp;&nbsp;</span>RGB</a></span></li></ul></li><li><span><a href="#RGB->YCrCb" data-toc-modified-id="RGB->YCrCb-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>RGB-&gt;YCrCb</a></span><ul class="toc-item"><li><span><a href="#RGB--->-HSV" data-toc-modified-id="RGB--->-HSV-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>RGB --&gt; HSV</a></span></li></ul></li><li><span><a href="#在图中画一条蓝线和一个红点" data-toc-modified-id="在图中画一条蓝线和一个红点-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>在图中画一条蓝线和一个红点</a></span></li></ul></div>


```python
import cv2
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.pyplot as plt
import imageio
import matplotlib.animation as animation
```

### pip install -i https://pypi.tuna.tsinghua.edu.cn/simple imageio-ffmpeg
### pip install -i https://pypi.tuna.tsinghua.edu.cn/simple imageio


```python
from IPython.display import HTML
```


```python
# 定义一个展示视频的函数
def display(driving, fps, size=(8, 6)):
    fig = plt.figure(figsize=size)

    ims = []
    for i in range(len(driving)):
        cols = []
        cols.append(driving[i])

        im = plt.imshow(np.concatenate(cols, axis=1), animated=True)
        plt.axis('off')
        ims.append([im])

    video = animation.ArtistAnimation(fig, ims, interval=1000.0/fps, repeat_delay=1000)

    plt.close()
    return video
```


```python
# 展示一下输入的视频, 如果视频太大，时间会非常久，可以跳过这个步骤
video_path = 'Peking_input360p_clip6_5s.mp4'
video_frames = imageio.mimread(video_path, memtest=False)

# 获得视频的原分辨率
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
    

HTML(display(video_frames, fps).to_html5_video())
```


```python
print('hello world')
```

    hello world
    

### 利用opencv读取图片并显示

<img src="./Picture/House256rgb.png" width="20%">


```python
img = cv2.imread('./Picture/House256rgb.png', 1) # 1 - RGB
cv2.imshow('Image', img)
cv2.waitKey()
cv2.destroyAllWindows() 
```


```python
img = cv2.imread('./Picture/House256rgb.png', 0) # 0 - grey
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
```


```python
img = cv2.imread('./Picture/House256rgb.png', 1)
print(type(img))
print(img.shape)
print(img[10, 8])
```

    <class 'numpy.ndarray'>
    (256, 256, 3)
    [222 197 157]
    


```python
img = cv2.imread('./Picture/House256rgb.png', 1) 
img_crop = img[:100, 100:180, :]
print(img_crop.shape)
cv2.imshow('Crop Image', img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows() 
```

    (100, 80, 3)
    


```python
img = cv2.imread('./Picture/House256rgb.png', 1)
print(img.shape)
plot.imshow(img)
plot.show()
```

    (256, 256, 3)
    


    
![png](output_13_1.png)
    


### RGB & BGR


```python
img = cv2.imread('./Picture/House256rgb.png', 1)
[b, g, r] = cv2.split(img)
img_rgb = cv2.merge([r, g, b])
plot.imshow(img_rgb)
plot.show()
```


    
![png](output_15_0.png)
    



```python
img = cv2.imread('./Picture/House256rgb.png', 1)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plot.imshow(img_rgb)
plot.show()
```


    
![png](output_16_0.png)
    



```python
plot.imshow(np.random.randn(256,256,3)*255)
plot.show()
```

    Clipping input data to the valid range for imshow with RGB data ([0..1] for floats or [0..255] for integers).
    


    
![png](output_17_1.png)
    


### 图像保存 JPEG和PNG


```python
img = cv2.imread('./Picture/House256rgb.png')
cv2.imwrite('imageTest_PNG.png', img)
```




    True




```python
img = cv2.imread('./Picture/House256rgb.png')
Quality = 80
cv2.imwrite('imageTest_JPEG_%d.jpg' % Quality, img, [cv2.IMWRITE_JPEG_QUALITY, Quality])
```




    True



### 颜色空间转换

### RGB 


```python
img = cv2.imread('./Picture/House256rgb.png')
# cv2.imshow('B', img[:,:,0])
# cv2.imshow('G', img[:,:,1])
# cv2.imshow('R', img[:,:,2])
cv2.waitKey(0)
```




    -1




```python
img = cv2.imread('./Picture/House256rgb.png')
print(img[:,:,0].shape)
plot.subplot(131)
plot.imshow(img[:,:,0], cmap='gray')  # B-G-R
plot.title('B')
plot.subplot(132)
plot.imshow(img[:,:,1], cmap='gray')
plot.title('G')
plot.subplot(133)
plot.imshow(img[:,:,2], cmap='gray')
plot.title('R')
plot.show()
```

    (256, 256)
    


    
![png](output_24_1.png)
    


## RGB->YCrCb


```python
# img = cv2.imread('./Picture/House256rgb.png')
# img_YCbCr = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# cv2.imshow('Y', img_YCbCr[:,:,0])
# cv2.imshow('Cb', img_YCbCr[:,:,1])
# cv2.imshow('Cr', img_YCbCr[:,:,2])
# cv2.waitKey(0)
```


```python
img = cv2.imread('./Picture/House256rgb.png')
img_YCbCr = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
plot.subplot(131)
plot.imshow(img_YCbCr[:,:,0], cmap='gray')
plot.title('Y')
plot.subplot(132)
plot.imshow(img_YCbCr[:,:,1], cmap='gray')
plot.title('Cr')
plot.subplot(133)
plot.imshow(img_YCbCr[:,:,2], cmap='gray')
plot.title('Cb')
plot.show()
```


    
![png](output_27_0.png)
    


### RGB --> HSV


```python
img = cv2.imread('./Picture/House256rgb.png')
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plot.subplot(131)
plot.imshow(img_HSV[:,:,0], cmap='gray')
plot.title('H')
plot.subplot(132)
plot.imshow(img_HSV[:,:,1], cmap='gray')
plot.title('S')
plot.subplot(133)
plot.imshow(img_HSV[:,:,2], cmap='gray')
plot.title('V')
plot.show()
```


    
![png](output_29_0.png)
    


## 在图中画一条蓝线和一个红点


```python
for k in range(0, 256):
    img[k, 100, :] = [255, 255, 0]  # b g r

img[200, 200] = [0, 0, 255]
    
cv2.imshow('image', img)
cv2.waitKey(0)
```




    -1




```python
disrow = 500
discol = 500
new_img = cv2.resize(img, (disrow, discol), interpolation = cv2.INTER_CUBIC)
cv2.imshow('new_img', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
```


```python
line_color = (0, 255, 0)
line_width = 2
x = 100
y = 200
w = 180
h = 90
cv2.rectangle(new_img, (x, y), (x + w, y + h), line_color, line_width)
cv2.imshow('new_img', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
```


```python
import cv2

cap = cv2.VideoCapture("video.avi")
while(1):
# 读取视频帧
    ret, frame = cap.read()
# 显示视频帧
    cv2.imshow("capture", frame)
#等候50ms,播放下一帧，或者按q键退出
if cv2.waitKey(50) &0xFF ==ord('q'):
    break
#释放视频流
cap.release()
#关闭所有窗口
cv2.destroyAllWindows()
```


```python

```


```python

```


```python

```


```python

```
