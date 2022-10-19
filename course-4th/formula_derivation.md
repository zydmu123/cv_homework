

$$
f=\|\max (X W, 0)-Y\|_F^2
$$

$$
f=\|\hat{Y}-Y\|_F^2  \quad  \quad \quad  \hat{Y} = max(Z,0) \quad \quad  \quad Z = XW
$$


$(1)$ $\frac{\partial f}{\partial W}$:

$$
\begin{aligned}
d f &=\operatorname{tr}\left(\frac{\partial f^{\top}}{\partial \hat{Y}} d \hat{Y}\right) \\
&=\operatorname{tr}\left(2 ((\hat{Y}-Y)\cdot \xi  )^{\top} d Z\right) \\
&=\operatorname{tr}\left(2 ((\hat{Y}-Y)\cdot \xi )^{\top}  X d W\right) \\
&=\operatorname{tr}\left(\left(2 X^{\top}((\hat{Y}-Y)\cdot \xi ) \right)^{\top} d W\right)
\end{aligned}
$$

$\Rightarrow$ $\frac{\partial f}{\partial W}=2 X^{\top}((\hat{Y}-Y)\cdot \xi)$ , $Note$:  $\xi$ = $np.where(z>0, 1, 0)$

$(2)$  $\frac{\partial f}{\partial X}$: 

$$
\begin{aligned}
d f &=\operatorname{tr}\left(\frac{\partial f^{\top}}{\partial \hat{Y}} d \hat{Y}\right) \\
&=\operatorname{tr}\left(2 ((\hat{Y}-Y) \cdot \xi )^{\top} d Z\right) \\
&=\operatorname{tr}\left(2 ((\hat{Y}-Y)  \cdot \xi )^{\top}  dX  W\right) \\
&=\operatorname{tr}\left(2 W\left((\hat{Y}-Y) \cdot \xi \right)^{\top} d X\right) \\
&=\operatorname{tr}\left( \left(\left(2(\hat{Y}-Y) \cdot \xi \right) W^{\top} \right)^{\top}d X\right)
\end{aligned}
$$        

$\Rightarrow$  $\frac{\partial f}{\partial X}=\left(2(\hat{Y}-Y) \cdot \xi \right) W^{\top}$, $Note$:  $\xi$ = $np.where(z>0, 1, 0)$

$(3)$ $\frac{\partial f}{\partial Y}$:

$$
\frac{\partial f}{\partial Y}=-2\left( \hat{Y}-Y \right)
$$

$(4)$ $Validation:$

![236ac22ef798ae8b60a97f6c120a3cc](https://user-images.githubusercontent.com/111970347/196576422-ebdd6be8-fcf6-44f6-a9c9-4dc5ba8cb68d.png)






