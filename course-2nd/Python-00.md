<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Python-基本数据类型" data-toc-modified-id="Python-基本数据类型-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Python 基本数据类型</a></span><ul class="toc-item"><li><span><a href="#List" data-toc-modified-id="List-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>List</a></span></li><li><span><a href="#Tuple" data-toc-modified-id="Tuple-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Tuple</a></span></li><li><span><a href="#Dict" data-toc-modified-id="Dict-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Dict</a></span></li><li><span><a href="#List-字面意思就是一个集合，在Python中List中的元素用中括号[-]来表示" data-toc-modified-id="List-字面意思就是一个集合，在Python中List中的元素用中括号[-]来表示-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>List 字面意思就是一个集合，在Python中List中的元素用中括号[ ]来表示</a></span></li><li><span><a href="#Tuple-可以看做是一种“不变”的List，访问也是通过下标，用小括号（）表示" data-toc-modified-id="Tuple-可以看做是一种“不变”的List，访问也是通过下标，用小括号（）表示-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Tuple 可以看做是一种“不变”的List，访问也是通过下标，用小括号（）表示</a></span></li><li><span><a href="#Dict-是Python中非常重要的数据类型，就像它的字面意思一样，它是个活字典，其实就是Key-Value键值对，可以用花括号{-}定义" data-toc-modified-id="Dict-是Python中非常重要的数据类型，就像它的字面意思一样，它是个活字典，其实就是Key-Value键值对，可以用花括号{-}定义-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Dict 是Python中非常重要的数据类型，就像它的字面意思一样，它是个活字典，其实就是Key-Value键值对，可以用花括号{ }定义</a></span></li></ul></li><li><span><a href="#测试" data-toc-modified-id="测试-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>测试</a></span></li><li><span><a href="#类-Class" data-toc-modified-id="类-Class-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>类 Class</a></span></li></ul></div>

## Python 基本数据类型
### List
### Tuple
### Dict


```python
print('Welcome to CV203!')
```

    Welcome to CV203!
    


```python
print("Welcome to CV203!")
# print("Welcome to Computer Vision C203!")
```

    Welcome to CV203!
    


```python
a = 3
b = 4
c = a + b
print(c)
print(type(c))
```

    7
    <class 'int'>
    


```python
print(a)
```

    3
    


```python
a = 3.
b = 4.
c = a + b
print(c)
print(type(c))
```

    7.0
    <class 'float'>
    

### List 字面意思就是一个集合，在Python中List中的元素用中括号[ ]来表示


```python
L = [12, 'China', 19.998]
print(L)
print(type(L))
```

    [12, 'China', 19.998]
    <class 'list'>
    


```python
L = []
print(L)
```

    []
    


```python
L = [12, 'China', 19.998]
print(L[0])
print(L[1])
print(L[2])
```

    12
    China
    19.998
    


```python
print(L[3])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Input In [9], in <cell line: 1>()
    ----> 1 print(L[3])
    

    IndexError: list index out of range



```python
print(L[-1])
```

    19.998
    


```python
print(L[-3])
```

    12
    


```python
print([L]*3)
```

    [[12, 'China', 19.998], [12, 'China', 19.998], [12, 'China', 19.998]]
    


```python
L = [12, 'China', 19.998]
print(L)
L.append('Jack')
print(L)
print(L[3])
```

    [12, 'China', 19.998]
    [12, 'China', 19.998, 'Jack']
    Jack
    


```python
L.pop()
print(L)
```

    [12, 'China', 19.998]
    


```python
L[1] = 1
print(L)
```

    [12, 1, 19.998]
    


```python
print(L[1:3])
```

    [1, 19.998]
    


```python
myName = 'David'
print(type(myName))
```

    <class 'str'>
    


```python
myName[0] = 'X'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [18], in <cell line: 1>()
    ----> 1 myName[0] = 'X'
    

    TypeError: 'str' object does not support item assignment


### Tuple 可以看做是一种“不变”的List，访问也是通过下标，用小括号（）表示


```python
t = (3.14, 'China', 'Jason')
print(t)
```

    (3.14, 'China', 'Jason')
    


```python
t[1] = 'America'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [20], in <cell line: 1>()
    ----> 1 t[1] = 'America'
    

    TypeError: 'tuple' object does not support item assignment



```python
t = ()
print(t)
```

    ()
    


```python
t = (3.14, )
print(t)
```

    (3.14,)
    


```python
a = [1,2,3,4]
print(a.insert(0,8))
print(a)
```

    None
    [8, 1, 2, 3, 4]
    

### Dict 是Python中非常重要的数据类型，就像它的字面意思一样，它是个活字典，其实就是Key-Value键值对，可以用花括号{ }定义


```python
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print(d)
```

    {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 75}
    


```python
len(d)
```




    4




```python
print(d)
d['Jone'] = 59
print(d)
```

    {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 75}
    {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 75, 'Jone': 59}
    


```python
print(d['Adam'])
```

    95
    


```python
d['Jack'] = 80
print(d)
```

    {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 75, 'Jone': 59, 'Jack': 80}
    


```python
d[0] = 'PKU'
print(d)
```

    {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 75, 'Jone': 59, 'Jack': 80, 0: 'PKU'}
    


```python
d['0']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Input In [30], in <cell line: 1>()
    ----> 1 d['0']
    

    KeyError: '0'



```python
if 'Adam' in d : 
    print('exist key')
else:
    print('No')
```

    exist key
    


```python
print(d.get('Adam'))
```

    95
    


```python
print(d.get('Jack'))
```

    80
    


```python
for key in d:
    print(key, ':', d.get(key))
```

    Adam : 95
    Lisa : 85
    Bart : 59
    Paul : 75
    Jone : 59
    Jack : 80
    0 : PKU
    

## 测试


```python
a = 3

print(a)

def myfun(x):
    x = x + 1
    return x

a = myfun(a)
print(a)
```

    3
    4
    


```python
a = 3

print(a)

def myfun(x):
    x = x + 1

myfun(a)
print(a)
```

    3
    3
    


```python
a = 3

def myfun(x):
    x = 1

myfun(a)
print(a)
```

    3
    


```python
a = [3, 4]
print(a)

def myfun(x):
    x[0] = 1

myfun(a)
print(a)
```

    [3, 4]
    [1, 4]
    


```python
a = {'0':3, '1': 5}

print(a)
```

    {'0': 3, '1': 5}
    


```python
   
def myfun(x):
    x[0] = 1

myfun(a)
print(a)
```

    {'0': 3, '1': 5, 0: 1}
    


```python
 
```

## 类 Class


```python
class Employee(object):
    empCount = 0
 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
 
    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary) 
       
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount) 
        
```

    Name :  Zara , Salary:  2000
    Name :  Manni , Salary:  5000
    Total Employee 2
    


```python

```


```python
class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print ('Hello, I am %s.' % self.name)

dog = Animal('dog3')
dog.greet() 
```

    Hello, I am dog3.
    


```python

```


```python
class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print ('Hello, I am %s.' % self.name)

class Dog(Animal):
    def greet(self):
        print ('WangWang.., I am %s. ' % self.name)

dog3 = Dog('dog3')
dog3.greet()
```

    WangWang.., I am dog3. 
    


```python
class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print ('Hello, I am %s.' % self.name)

class Dog(Animal):
    def greet(self):
        super(Dog, self).greet()
        print ('WangWang...')

dog3 = Dog('dog3')
dog3.greet()
```

    Hello, I am dog3.
    WangWang...
    


```python

```
