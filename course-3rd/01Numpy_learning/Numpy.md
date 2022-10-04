<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#What-is-NumPy?" data-toc-modified-id="What-is-NumPy?-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>What is NumPy?</a></span></li><li><span><a href="#Installation-of-NumPy" data-toc-modified-id="Installation-of-NumPy-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Installation of NumPy</a></span></li><li><span><a href="#Import-NumPy" data-toc-modified-id="Import-NumPy-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Import NumPy</a></span><ul class="toc-item"><li><span><a href="#What-is-Vectorization?" data-toc-modified-id="What-is-Vectorization?-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>What is Vectorization?</a></span></li></ul></li><li><span><a href="#NumPy-as-np" data-toc-modified-id="NumPy-as-np-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>NumPy as np</a></span></li><li><span><a href="#Checking-NumPy-Version" data-toc-modified-id="Checking-NumPy-Version-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Checking NumPy Version</a></span></li><li><span><a href="#Create-a-NumPy-ndarray-Object" data-toc-modified-id="Create-a-NumPy-ndarray-Object-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Create a NumPy ndarray Object</a></span></li><li><span><a href="#Dimensions-in-Arrays" data-toc-modified-id="Dimensions-in-Arrays-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Dimensions in Arrays</a></span></li><li><span><a href="#0-D-Arrays" data-toc-modified-id="0-D-Arrays-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>0-D Arrays</a></span></li><li><span><a href="#1-D-Arrays" data-toc-modified-id="1-D-Arrays-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>1-D Arrays</a></span></li><li><span><a href="#2-D-Arrays" data-toc-modified-id="2-D-Arrays-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>2-D Arrays</a></span></li><li><span><a href="#3-D-arrays" data-toc-modified-id="3-D-arrays-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>3-D arrays</a></span></li><li><span><a href="#Check-Number-of-Dimensions?" data-toc-modified-id="Check-Number-of-Dimensions?-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>Check Number of Dimensions?</a></span></li><li><span><a href="#Access-Array-Elements" data-toc-modified-id="Access-Array-Elements-13"><span class="toc-item-num">13&nbsp;&nbsp;</span>Access Array Elements</a></span></li><li><span><a href="#Access-2-D-Arrays" data-toc-modified-id="Access-2-D-Arrays-14"><span class="toc-item-num">14&nbsp;&nbsp;</span>Access 2-D Arrays</a></span></li><li><span><a href="#Access-3-D-Arrays" data-toc-modified-id="Access-3-D-Arrays-15"><span class="toc-item-num">15&nbsp;&nbsp;</span>Access 3-D Arrays</a></span></li><li><span><a href="#Negative-Indexing" data-toc-modified-id="Negative-Indexing-16"><span class="toc-item-num">16&nbsp;&nbsp;</span>Negative Indexing</a></span></li><li><span><a href="#Slicing-Arrays" data-toc-modified-id="Slicing-Arrays-17"><span class="toc-item-num">17&nbsp;&nbsp;</span>Slicing Arrays</a></span></li><li><span><a href="#Negative-Slicing" data-toc-modified-id="Negative-Slicing-18"><span class="toc-item-num">18&nbsp;&nbsp;</span>Negative Slicing</a></span></li><li><span><a href="#STEP" data-toc-modified-id="STEP-19"><span class="toc-item-num">19&nbsp;&nbsp;</span>STEP</a></span></li><li><span><a href="#Slicing-2-D-Arrays" data-toc-modified-id="Slicing-2-D-Arrays-20"><span class="toc-item-num">20&nbsp;&nbsp;</span>Slicing 2-D Arrays</a></span></li><li><span><a href="#Data-Types-in-NumPy" data-toc-modified-id="Data-Types-in-NumPy-21"><span class="toc-item-num">21&nbsp;&nbsp;</span>Data Types in NumPy</a></span></li><li><span><a href="#Checking-the-Data-Type-of-an-Array" data-toc-modified-id="Checking-the-Data-Type-of-an-Array-22"><span class="toc-item-num">22&nbsp;&nbsp;</span>Checking the Data Type of an Array</a></span></li><li><span><a href="#Converting-Data-Type-on-Existing-Arrays" data-toc-modified-id="Converting-Data-Type-on-Existing-Arrays-23"><span class="toc-item-num">23&nbsp;&nbsp;</span>Converting Data Type on Existing Arrays</a></span></li><li><span><a href="#NumPy-Array-Copy-vs-View" data-toc-modified-id="NumPy-Array-Copy-vs-View-24"><span class="toc-item-num">24&nbsp;&nbsp;</span>NumPy Array Copy vs View</a></span></li><li><span><a href="#Check-if-Array-Owns-it's-Data" data-toc-modified-id="Check-if-Array-Owns-it's-Data-25"><span class="toc-item-num">25&nbsp;&nbsp;</span>Check if Array Owns it's Data</a></span></li><li><span><a href="#Shape-of-an-Array" data-toc-modified-id="Shape-of-an-Array-26"><span class="toc-item-num">26&nbsp;&nbsp;</span>Shape of an Array</a></span></li><li><span><a href="#Reshaping-arrays" data-toc-modified-id="Reshaping-arrays-27"><span class="toc-item-num">27&nbsp;&nbsp;</span>Reshaping arrays</a></span></li><li><span><a href="#Reshape-From-1-D-to-2-D" data-toc-modified-id="Reshape-From-1-D-to-2-D-28"><span class="toc-item-num">28&nbsp;&nbsp;</span>Reshape From 1-D to 2-D</a></span></li><li><span><a href="#Reshape-From-1-D-to-3-D" data-toc-modified-id="Reshape-From-1-D-to-3-D-29"><span class="toc-item-num">29&nbsp;&nbsp;</span>Reshape From 1-D to 3-D</a></span></li><li><span><a href="#Unknown-Dimension" data-toc-modified-id="Unknown-Dimension-30"><span class="toc-item-num">30&nbsp;&nbsp;</span>Unknown Dimension</a></span></li><li><span><a href="#Flattening-the-arrays" data-toc-modified-id="Flattening-the-arrays-31"><span class="toc-item-num">31&nbsp;&nbsp;</span>Flattening the arrays</a></span></li><li><span><a href="#Iterating-Arrays" data-toc-modified-id="Iterating-Arrays-32"><span class="toc-item-num">32&nbsp;&nbsp;</span>Iterating Arrays</a></span></li><li><span><a href="#Joining-NumPy-Arrays" data-toc-modified-id="Joining-NumPy-Arrays-33"><span class="toc-item-num">33&nbsp;&nbsp;</span>Joining NumPy Arrays</a></span></li><li><span><a href="#Joining-Arrays-Using-Stack-Functions" data-toc-modified-id="Joining-Arrays-Using-Stack-Functions-34"><span class="toc-item-num">34&nbsp;&nbsp;</span>Joining Arrays Using Stack Functions</a></span></li><li><span><a href="#Stacking-Along-Rows" data-toc-modified-id="Stacking-Along-Rows-35"><span class="toc-item-num">35&nbsp;&nbsp;</span>Stacking Along Rows</a></span></li><li><span><a href="#Stacking-Along-Columns" data-toc-modified-id="Stacking-Along-Columns-36"><span class="toc-item-num">36&nbsp;&nbsp;</span>Stacking Along Columns</a></span></li><li><span><a href="#Splitting-NumPy-Arrays" data-toc-modified-id="Splitting-NumPy-Arrays-37"><span class="toc-item-num">37&nbsp;&nbsp;</span>Splitting NumPy Arrays</a></span></li><li><span><a href="#Splitting-2-D-Arrays" data-toc-modified-id="Splitting-2-D-Arrays-38"><span class="toc-item-num">38&nbsp;&nbsp;</span>Splitting 2-D Arrays</a></span></li><li><span><a href="#Searching-Arrays" data-toc-modified-id="Searching-Arrays-39"><span class="toc-item-num">39&nbsp;&nbsp;</span>Searching Arrays</a></span></li><li><span><a href="#Sorting-Arrays" data-toc-modified-id="Sorting-Arrays-40"><span class="toc-item-num">40&nbsp;&nbsp;</span>Sorting Arrays</a></span></li><li><span><a href="#Filtering-Arrays" data-toc-modified-id="Filtering-Arrays-41"><span class="toc-item-num">41&nbsp;&nbsp;</span>Filtering Arrays</a></span></li><li><span><a href="#Generate-Random-Number" data-toc-modified-id="Generate-Random-Number-42"><span class="toc-item-num">42&nbsp;&nbsp;</span>Generate Random Number</a></span></li><li><span><a href="#Generate-Random-Float" data-toc-modified-id="Generate-Random-Float-43"><span class="toc-item-num">43&nbsp;&nbsp;</span>Generate Random Float</a></span></li><li><span><a href="#Generate-Random-Number-From-Array" data-toc-modified-id="Generate-Random-Number-From-Array-44"><span class="toc-item-num">44&nbsp;&nbsp;</span>Generate Random Number From Array</a></span></li><li><span><a href="#Random-Permutations" data-toc-modified-id="Random-Permutations-45"><span class="toc-item-num">45&nbsp;&nbsp;</span>Random Permutations</a></span></li><li><span><a href="#Normal-Distribution" data-toc-modified-id="Normal-Distribution-46"><span class="toc-item-num">46&nbsp;&nbsp;</span>Normal Distribution</a></span></li><li><span><a href="#Uniform-Distribution" data-toc-modified-id="Uniform-Distribution-47"><span class="toc-item-num">47&nbsp;&nbsp;</span>Uniform Distribution</a></span><ul class="toc-item"><li><span><a href="#Brief-Summary" data-toc-modified-id="Brief-Summary-47.1"><span class="toc-item-num">47.1&nbsp;&nbsp;</span>Brief Summary</a></span></li></ul></li><li><span><a href="#Array-Operations/Math" data-toc-modified-id="Array-Operations/Math-48"><span class="toc-item-num">48&nbsp;&nbsp;</span>Array Operations/Math</a></span></li></ul></div>


```python
from PIL import Image
```


```python
# path = "imgs/1200px-NumPy_logo_2020.svg.png"
path = "numpyLogo.jpg"
display(Image.open(path))
```


    
![png](output_2_0.png)
    


https://numpy.org/

### What is NumPy?

NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

NumPy stands for Numerical Python.

Why Use NumPy?

Why is NumPy Faster Than Lists?

Which Language is NumPy written in?

### Installation of NumPy


```python
!pip install numpy
```

### Import NumPy


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
```

    [1 2 3 4 5]
    <class 'numpy.ndarray'>
    

#### What is Vectorization?

Converting iterative statements into a vector based operation is called vectorization.

It is faster as modern CPUs are optimized for such operations.

Without Numpy:


```python
%%time
a = [i for i in range(100000)]
b = [i for i in range(100000)]
```

    CPU times: total: 0 ns
    Wall time: 4.61 ms
    


```python
%%time
c = []
for i in range(len(a)):
    c.append(a[i] + 2 * b[i])
```

    CPU times: total: 15.6 ms
    Wall time: 21.6 ms
    

With Numpy:


```python
%%time
a = np.arange(100000)
b = np.arange(100000)
```

    CPU times: total: 0 ns
    Wall time: 1.95 ms
    


```python
%%time
c = a + 2 * b
```

    CPU times: total: 0 ns
    Wall time: 2.08 ms
    

### NumPy as np


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```

    [1 2 3 4 5]
    

### Checking NumPy Version


```python
import numpy as np

print(np.__version__)
```

    1.23.3
    

### Create a NumPy ndarray Object


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
```

    [1 2 3 4 5]
    <class 'numpy.ndarray'>
    


```python
import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)
print(type(arr))
```

    [1 2 3 4 5]
    <class 'numpy.ndarray'>
    

### Dimensions in Arrays

### 0-D Arrays


```python
import numpy as np

arr = np.array(42)

print(arr)
print(type(arr))
```

    42
    <class 'numpy.ndarray'>
    


```python

```

### 1-D Arrays


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))
```

    [1 2 3 4 5]
    <class 'numpy.ndarray'>
    

### 2-D Arrays


```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
print(type(arr))
```

    [[1 2 3]
     [4 5 6]]
    <class 'numpy.ndarray'>
    

### 3-D arrays


```python
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)
```

    [[[1 2 3]
      [4 5 6]]
    
     [[1 2 3]
      [4 5 6]]]
    

### Check Number of Dimensions?


```python
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
```

    0
    1
    2
    3
    

### Access Array Elements


```python
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
```

    1
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])
```

    2
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])
```

    7
    

### Access 2-D Arrays


```python
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
```

    2nd element on 1st row:  2
    


```python
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])
```

    5th element on 2nd row:  10
    

### Access 3-D Arrays


```python
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr[0, 1, 2])
```

    [[[ 1  2  3]
      [ 4  5  6]]
    
     [[ 7  8  9]
      [10 11 12]]]
    6
    

### Negative Indexing


```python
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

dim = arr.ndim

print(dim)

print('Last element from 2nd dim: ', arr[1, -1])
```

    2
    Last element from 2nd dim:  10
    

### Slicing Arrays


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7]) 

print(arr[1:5])
```

    [2 3 4 5]
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])
```

    [5 6 7]
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])
```

    [1 2 3 4]
    

### Negative Slicing


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1]) # 前闭后开
```

    [5 6]
    

### STEP


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:6:2]) # the last para is step
```

    [2 4 6]
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])
```

    [1 3 5 7]
    

### Slicing 2-D Arrays


```python
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
```

    [7 8 9]
    


```python
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])
```

    [3 8]
    


```python
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])
```

    [[2 3 4]
     [7 8 9]]
    

### Data Types in NumPy

NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer

b - boolean

u - unsigned integer

f - float

c - complex float

m - timedelta

M - datetime

O - object

S - string

U - unicode string

V - fixed chunk of memory for other type ( void )

### Checking the Data Type of an Array


```python
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)
```

    int32
    


```python
import numpy as np

arr = np.array([1.2, 2, 3, 4])

print(arr.dtype)
```

    float64
    


```python
import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)
```

    <U6
    


```python
print(arr)
```

    ['apple' 'banana' 'cherry']
    

### Converting Data Type on Existing Arrays


```python
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)
```

    [1 2 3]
    int32
    


```python
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)
```

    [1 2 3]
    int32
    


```python
import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
```

    [ True False  True]
    bool
    

### NumPy Array Copy vs View


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() # 浅拷贝
arr[0] = 42

print(arr)
print(x)
```

    [42  2  3  4  5]
    [1 2 3 4 5]
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view() # 深拷贝
arr[0] = 42

print(arr)
print(x)
```

    [42  2  3  4  5]
    [42  2  3  4  5]
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr
x[0] = 31

print(arr)
print(x)
```

    [31  2  3  4  5]
    [31  2  3  4  5]
    

The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

### Check if Array Owns it's Data


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr.base)   # ????

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
```

    None
    None
    [1 2 3 4 5]
    

### Shape of an Array


```python
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)
```

    (2, 4)
    


```python
row, col = arr.shape
print(row)
print(col)
```

    2
    4
    

### Reshaping arrays

Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.

### Reshape From 1-D to 2-D



```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 6)

print(newarr)
```

    [[ 1  2  3  4  5  6]
     [ 7  8  9 10 11 12]]
    

### Reshape From 1-D to 3-D


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)
```

    [[[ 1  2]
      [ 3  4]
      [ 5  6]]
    
     [[ 7  8]
      [ 9 10]
      [11 12]]]
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(3, 3)

print(newarr)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Input In [55], in <cell line: 5>()
          1 import numpy as np
          3 arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    ----> 5 newarr = arr.reshape(3, 3)
          7 print(newarr)
    

    ValueError: cannot reshape array of size 8 into shape (3,3)



```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = arr.reshape(2, 4)  # “深拷贝”？

print(arr.base)
print(x.base)
x[0,1] = 10
print(x)
print(arr)
```

    None
    [1 2 3 4 5 6 7 8]
    [[ 1 10  3  4]
     [ 5  6  7  8]]
    [ 1 10  3  4  5  6  7  8]
    

### Unknown Dimension


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, -1, 2)

print(newarr)
```

    [[[1 2]
      [3 4]]
    
     [[5 6]
      [7 8]]]
    

### Flattening the arrays



```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)   # -1 means Flattening ?

print(newarr)
```

    [1 2 3 4 5 6]
    

### Iterating Arrays



```python
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)
```

    1
    2
    3
    


```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)
```

    [1 2 3]
    [4 5 6]
    


```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print(y)
```

    1
    2
    3
    4
    5
    6
    


```python
row,col = arr.shape

for i in range(row):
    for j in range(col):
        print(arr[i][j])
```

    1
    2
    3
    4
    5
    6
    


```python
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:  # x 的单位是“次一维”
    print(x)
```

    [[1 2 3]
     [4 5 6]]
    [[ 7  8  9]
     [10 11 12]]
    

### Joining NumPy Arrays


```python
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)
```

    [1 2 3 4 5 6]
    


```python
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

print(arr1)
print(arr2)
print('\n')
arr = np.concatenate((arr1, arr2), axis=0) # 按行拼接
print(arr)
print('\n')
arr = np.concatenate((arr1, arr2), axis=1) # 按列拼接
print(arr)
```

    [[1 2]
     [3 4]]
    [[5 6]
     [7 8]]
    
    
    [[1 2]
     [3 4]
     [5 6]
     [7 8]]
    
    
    [[1 2 5 6]
     [3 4 7 8]]
    

### Joining Arrays Using Stack Functions



```python
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=0)

print(arr)
```

    [[1 2 3]
     [4 5 6]]
    

### Stacking Along Rows



```python
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr1.ndim)

print(arr)
```

    1
    [1 2 3 4 5 6]
    

### Stacking Along Columns



```python
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)
```

    [[1 2 3]
     [4 5 6]]
    

### Splitting NumPy Arrays


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
```

    [array([1, 2]), array([3, 4]), array([5, 6])]
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)
```

    [array([1, 2]), array([3, 4]), array([5]), array([6])]
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])
```

    [1 2]
    [3 4]
    [5 6]
    

### Splitting 2-D Arrays



```python
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])


print(arr.shape)
newarr = np.array_split(arr, 3)

print(newarr)
```

    (6, 2)
    [array([[1, 2],
           [3, 4]]), array([[5, 6],
           [7, 8]]), array([[ 9, 10],
           [11, 12]])]
    


```python
print(arr.shape)
print(newarr[0])
print(newarr[1])
print(newarr[2])
```

    (6, 2)
    [[1 2]
     [3 4]]
    [[5 6]
     [7 8]]
    [[ 9 10]
     [11 12]]
    


```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)
```

    [array([[1, 2, 3],
           [4, 5, 6]]), array([[ 7,  8,  9],
           [10, 11, 12]]), array([[13, 14, 15],
           [16, 17, 18]])]
    


```python
print(arr.shape)
print(newarr[0])
print(newarr[1])
print(newarr[2])
```

    (6, 3)
    [[1 2 3]
     [4 5 6]]
    [[ 7  8  9]
     [10 11 12]]
    [[13 14 15]
     [16 17 18]]
    

### Searching Arrays



```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
```

    (array([3, 5, 6], dtype=int64),)
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)
```

    (array([1, 3, 5, 7], dtype=int64),)
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)
```

    (array([0, 2, 4, 6], dtype=int64),)
    

### Sorting Arrays



```python
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))
```

    [0 1 2 3]
    


```python
print(np.sort(arr).base)
```

    None
    


```python
import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))
```

    ['apple' 'banana' 'cherry']
    


```python
import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr))
```

    [False  True  True]
    


```python
import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
```

    [[2 3 4]
     [0 1 5]]
    

### Filtering Arrays

Getting some elements out of an existing array and creating a new array out of them is called filtering.

In NumPy, you filter an array using a boolean index list.


```python
import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)
```

    [41 43]
    


```python
import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
```

    [False, False, True, True]
    [43 44]
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
```

    [False, True, False, True, False, True, False]
    [2 4 6]
    


```python
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42
print(filter_arr)
```

    [False False  True  True]
    


```python


newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
```

    [False False  True  True]
    [43 44]
    


```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
```

    [False  True False  True False  True False]
    [2 4 6]
    

### Generate Random Number



```python
from numpy import random

x = random.randint(100)

print(x)
```

    71
    


```python
x = random.randint(100)

print(x)
```

    34
    

### Generate Random Float



```python
from numpy import random

x = random.rand()

print(x)
```

    0.9828808578474523
    


```python
from numpy import random

x=random.randint(100, size=(5))

print(x)
```

    [48 41  5 89 10]
    


```python
from numpy import random

x = random.randint(100, size=(3, 5))

print(x)
```

    [[95 43 34 93 63]
     [56 71 87 68 75]
     [62 28 89 38 10]]
    


```python
from numpy import random

x = random.rand(5)

print(x)
```

    [0.42206151 0.11130478 0.05035759 0.92103222 0.36807312]
    


```python
from numpy import random

x = random.rand(3, 5)

print(x)
```

    [[0.18279162 0.33804692 0.47873173 0.65673516 0.15349512]
     [0.10465625 0.22882666 0.78405362 0.39509292 0.07949781]
     [0.84911905 0.80702164 0.16185306 0.43559487 0.55757135]]
    


```python

```


```python

```

### Generate Random Number From Array


```python
from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)
```

    9
    


```python
from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)
```

    [[3 3 9 9 5]
     [7 7 3 3 5]
     [3 9 5 5 7]]
    

### Random Permutations



```python
# Shuffling Arrays
```


```python
from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)
print(arr)
```

    [5 4 2 1 3]
    


```python
# Generating Permutation of Arrays
```


```python
from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))
```

    [1 5 2 3 4]
    

### Normal Distribution



```python
from numpy import random

x = random.normal(size=(2, 3))

print(x)
```

    [[ 0.0359605   0.73916151 -2.88052907]
     [-0.79573651 -2.37757676  1.57539782]]
    

### Uniform Distribution


```python
from numpy import random

x = random.uniform(size=(2, 3))

print(x)
```

    [[0.40211199 0.51105688 0.05787912]
     [0.31404287 0.1378343  0.84551062]]
    


```python

```

#### Brief Summary


```python
a = np.array([1, 2, 3])   
print(type(a))           
print(a.shape)            
print(a[0], a[1], a[2]) 
a[0] = 5                  
print(a)                  
```

    <class 'numpy.ndarray'>
    (3,)
    1 2 3
    [5 2 3]
    


```python
b = np.array([[1, 2, 3],
              [4, 5, 6]])    
print(b.shape)                     
print(b[0, 0], b[0, 1], b[1, 0])  
```

    (2, 3)
    1 2 4
    


```python
print(type(b.shape))
```

    <class 'tuple'>
    


```python
# Other Initializations
import numpy as np
```


```python
a = np.zeros((2, 2)) 
print(a)
```

    [[0. 0.]
     [0. 0.]]
    


```python
b = np.full((2, 2), 7)
print(b)
```

    [[7 7]
     [7 7]]
    


```python
c = np.eye(3)
print(c)
```

    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    


```python
d = np.random.random((2, 2))
print(d)
```

    [[0.63054819 0.04140086]
     [0.04584985 0.31271472]]
    


```python
a = np.ones((2, 2))  
print(a)   
```

    [[1. 1.]
     [1. 1.]]
    


```python
nums = np.arange(8)
print(nums)
print(nums.min())
print(np.min(nums))
```

    [0 1 2 3 4 5 6 7]
    0
    0
    


```python
np.linspace(-1, 1, 5)
```




    array([-1. , -0.5,  0. ,  0.5,  1. ])




```python
np.linspace(-1, 1, 100).shape
```




    (100,)



### Array Operations/Math


```python
x = np.array([[1, 2],
              [3, 4]], dtype='f')
y = np.array([[5, 6],
              [7, 8]], dtype='f')
```


```python
print(x)
print(y)
```

    [[0.40211199 0.51105688 0.05787912]
     [0.31404287 0.1378343  0.84551062]]
    6
    


```python
print(x + y)
print(np.add(x, y))
```

    [[6.40211199 6.51105688 6.05787912]
     [6.31404287 6.1378343  6.84551062]]
    [[6.40211199 6.51105688 6.05787912]
     [6.31404287 6.1378343  6.84551062]]
    


```python
print(x - y)
print(np.subtract(x, y))
```

    [[-5.59788801 -5.48894312 -5.94212088]
     [-5.68595713 -5.8621657  -5.15448938]]
    [[-5.59788801 -5.48894312 -5.94212088]
     [-5.68595713 -5.8621657  -5.15448938]]
    


```python
print(x * y)
print(np.multiply(x, y))
```

    [[2.41267197 3.06634126 0.34727472]
     [1.88425723 0.8270058  5.07306374]]
    [[2.41267197 3.06634126 0.34727472]
     [1.88425723 0.8270058  5.07306374]]
    


```python
print(np.sqrt(x))
```

    [[0.63412301 0.71488242 0.2405808 ]
     [0.56039528 0.37126042 0.91951652]]
    


```python
print(x / y)
print(np.divide(x, y))
```

    [[0.06701867 0.08517615 0.00964652]
     [0.05234048 0.02297238 0.14091844]]
    [[0.06701867 0.08517615 0.00964652]
     [0.05234048 0.02297238 0.14091844]]
    


```python

```


```python
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w))
```

    219
    


```python
print(np.dot(v, w))
```

    219
    


```python
print(x.dot(v))
print(np.dot(x, v))
```

    [29 67]
    [29 67]
    


```python
print(x.dot(y))
print(np.dot(x, y))
```

    [[19 22]
     [43 50]]
    [[19 22]
     [43 50]]
    


```python

```


```python
x = np.array([[1, 2, 3], 
              [4, 5, 6]])

print(np.sum(x))          
```

    21
    


```python
print(np.sum(x, axis=0))
```

    [5 7 9]
    


```python
print(np.sum(x, axis=1)) 
```

    [ 6 15]
    


```python
print(np.max(x, axis=1))
```

    [3 6]
    


```python
x = np.array([[1, 2, 3],
              [3, 5, 7]])
print(x * 2) 
```

    [[ 2  4  6]
     [ 6 10 14]]
    


```python

```
