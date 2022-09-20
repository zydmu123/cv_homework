<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Comments" data-toc-modified-id="Comments-0.1"><span class="toc-item-num">0.1&nbsp;&nbsp;</span>Comments</a></span><ul class="toc-item"><li><span><a href="#Comments-can-be-used-to-explain-Python-code." data-toc-modified-id="Comments-can-be-used-to-explain-Python-code.-0.1.1"><span class="toc-item-num">0.1.1&nbsp;&nbsp;</span>Comments can be used to explain Python code.</a></span></li><li><span><a href="#Comments-can-be-used-to-make-the-code-more-readable." data-toc-modified-id="Comments-can-be-used-to-make-the-code-more-readable.-0.1.2"><span class="toc-item-num">0.1.2&nbsp;&nbsp;</span>Comments can be used to make the code more readable.</a></span></li><li><span><a href="#Comments-can-be-used-to-prevent-execution-when-testing-code." data-toc-modified-id="Comments-can-be-used-to-prevent-execution-when-testing-code.-0.1.3"><span class="toc-item-num">0.1.3&nbsp;&nbsp;</span>Comments can be used to prevent execution when testing code.</a></span></li></ul></li></ul></li><li><span><a href="#Syntax" data-toc-modified-id="Syntax-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Syntax</a></span></li><li><span><a href="#If-...-Else" data-toc-modified-id="If-...-Else-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>If ... Else</a></span></li><li><span><a href="#Complex-Types" data-toc-modified-id="Complex-Types-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Complex Types</a></span><ul class="toc-item"><li><span><a href="#List" data-toc-modified-id="List-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>List</a></span></li><li><span><a href="#Tuple" data-toc-modified-id="Tuple-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Tuple</a></span></li><li><span><a href="#Dictionary" data-toc-modified-id="Dictionary-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Dictionary</a></span></li><li><span><a href="#Set" data-toc-modified-id="Set-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Set</a></span></li><li><span><a href="#Tuple" data-toc-modified-id="Tuple-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Tuple</a></span></li></ul></li></ul></div>


```python

```

### Comments
#### Comments can be used to explain Python code.
#### Comments can be used to make the code more readable.
#### Comments can be used to prevent execution when testing code.


```python
#This is a comment
print("Hello, World!")
```

    Hello, World!
    


```python
print("Hello, World!") #This is a comment
```

    Hello, World!
    


```python
#This is a comment
#written in
#more than just one line
print("Hello, World!")
```

    Hello, World!
    


```python
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
```

    Hello, World!
    

## Syntax


```python
if 5 > 2:
print("Five is greater than two!")
```


      Input In [5]
        print("Five is greater than two!")
        ^
    IndentationError: expected an indented block
    



```python
if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
    print("Five is greater than two!")
```

    Five is greater than two!
    Five is greater than two!
    


```python
if 5 > 2:
    print("Five is greater than two!")
```

    Five is greater than two!
    


```python
## Type 
```


```python
x = "Hello World"
print(type(x))
```

    <class 'str'>
    


```python
x = "Hello World"
print(type(x))
```

    <class 'str'>
    


```python
x = 20.5
print(type(x))
```

    <class 'float'>
    


```python
x = 20
print(type(x))
```

    <class 'int'>
    


```python
x = ["apple", "banana", "cherry"]
print(type(x))
```

    <class 'list'>
    


```python
x = ("apple", "banana", "cherry")
print(type(x))
```

    <class 'tuple'>
    


```python
x = {"name" : "John", "age" : 36}
print(type(x))
```

    <class 'dict'>
    


```python
x = range(6)
print(type(x))
```

    <class 'range'>
    


```python

```


```python
# Boolean Values
```


```python
print(10 > 9)
print(10 == 9)
print(10 < 9)
```

    True
    False
    False
    


```python
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
```

    b is not greater than a
    


```python
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
```

    True
    True
    


```python
x = ""
y = None
z = 0


print(bool(x))
print(bool(y))
print(bool(z))
```

    False
    False
    False
    

## If ... Else


```python
a = 33
b = 200
if b > a:
    print("b is greater than a") 
```

    b is greater than a
    


```python
a = 33
b = 200
if a <= b: print("a is greater than b")
```

    a is greater than b
    


```python
a = 2
b = 1
print("A") if a > b else print("B")
```

    A
    


```python
# Compute the sum of 2,3,4,5,6,7,8,9,10
```


```python
num = 10
sum = 0
for i in range(2,num+1):
    sum = sum + i 
print(sum)
```

    54
    


```python
sum = 0
i = 0
while i < 10:
    i = i + 1
    sum = sum + i 
print(sum)
```

    55
    


```python

```

## Complex Types
### List
### Tuple
### Dictionary
### Set


```python
### List
```


```python
# Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

    ['apple', 'banana', 'cherry']
    


```python
# List items are ordered, changeable, and allow duplicate values.
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
```

    ['apple', 'banana', 'cherry', 'apple', 'cherry']
    


```python
# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```

    3
    


```python
# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
```


```python
list = [1,212,'s']
```


```python
# List Type
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))
```

    <class 'list'>
    <class 'list'>
    <class 'list'>
    <class 'list'>
    


```python
## list() Constructor
thislist = list(("apple", 12, "ww")) 
print(thislist)   
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [31], in <cell line: 2>()
          1 ## list() Constructor
    ----> 2 thislist = list(("apple", 12, "ww")) 
          3 print(thislist)
    

    TypeError: 'list' object is not callable



```python
# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
```

    banana
    


```python
# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```

    cherry
    


```python
# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:3])
print(thislist[2])
```

    ['cherry']
    cherry
    


```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
```

    ['apple', 'banana', 'cherry', 'orange']
    


```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:-1])
```

    ['cherry', 'orange', 'kiwi', 'melon']
    


```python
# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
```

    ['orange', 'kiwi', 'melon']
    


```python
# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "appl" in thislist:
    print("Yes, 'apple' is in the fruits list")
else:
    print('Wrong')
```

    Wrong
    


```python
# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = [12,'apple']
print(thislist)
```

    ['apple', [12, 'apple'], 'cherry']
    


```python
# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) 
```

    ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
    


```python
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
```

    ['apple', 'blackcurrant', 'watermelon', 'cherry']
    


```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = ["blackcurrant", "watermelon"]
print(thislist)
```

    ['apple', ['blackcurrant', 'watermelon'], 'cherry']
    


```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1:3])
thislist[1:3] = ["watermelon"]
print(thislist)
```

    ['banana', 'cherry']
    ['apple', 'watermelon']
    


```python

```


```python
# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append(12)
print(thislist)
```

    ['apple', 'banana', 'cherry', 12]
    


```python
# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, 12)
print(thislist)
```

    ['apple', 'banana', 12, 'cherry']
    


```python
# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
tropical.extend(thislist)
print(tropical)
print(thislist)
```

    ['mango', 'pineapple', 'papaya', 'apple', 'banana', 'cherry']
    ['apple', 'banana', 'cherry']
    


```python
# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
```

    ['apple', 'banana', 'cherry', 'kiwi', 'orange']
    


```python
# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
```

    ['apple', 'cherry']
    


```python
# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
```

    ['apple', 'cherry']
    


```python
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
```

    ['apple', 'banana']
    


```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
```

    ['banana', 'cherry']
    


```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
del thislist
print(thislist)
```

    ['apple', 'banana', 'cherry']
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [52], in <cell line: 4>()
          2 print(thislist)
          3 del thislist
    ----> 4 print(thislist)
    

    NameError: name 'thislist' is not defined



```python
# Clear the List
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print(thislist)
```

    ['apple', 'banana', 'cherry']
    []
    


```python
# Loop Through a List
thislist = [1,2,3,4,5]
sum = 0
for x in thislist:
    sum = sum + x
    print(x)
print(sum)
```

    1
    2
    3
    4
    5
    15
    


```python
mylist = []
mylist.append('apple')
print(mylist)
```

    ['apple']
    


```python
# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry", 4]
for i in range(len(thislist)):
    print(thislist[i])
for x in thislist:
    print(x)
```

    apple
    banana
    cherry
    4
    apple
    banana
    cherry
    4
    


```python
# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
```

    apple
    banana
    cherry
    


```python
# List Comprehension
```


```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```

    ['apple', 'banana', 'mango']
    


```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "k" in x]
# newlist = [x for x in fruits]
print(newlist)
```

    ['kiwi']
    


```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]
print(newlist)
```

    ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
    


```python
newlist = ['hello' for x in fruits]
print(newlist)
```

    ['hello', 'hello', 'hello', 'hello', 'hello']
    


```python
newlist = [x for x in range(10) if x < 5]
print(newlist)
```

    [0, 1, 2, 3, 4]
    


```python

```


```python
# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
```

    ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
    


```python
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
```

    [23, 50, 65, 82, 100]
    


```python
# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
```

    ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
    


```python
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
```

    [100, 82, 65, 50, 23]
    


```python
# Customize Sort Function
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) # first run the myFunc() on those nums, then,sort those nums(original values) according to runned-results
print(thislist)
```

    [50, 65, 23, 82, 100]
    


```python
# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
```

    ['Kiwi', 'Orange', 'banana', 'cherry']
    


```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
```

    ['banana', 'cherry', 'Kiwi', 'Orange']
    


```python
# Copy a List
thislist = ["apple", "banana", "cherry"]
print(thislist)
# mylist = thislist.copy()
# print(mylist)
```

    ['apple', 'banana', 'cherry']
    


```python
mylist = thislist.copy()
print(mylist)
a = list([1])
print(a)
```

    ['apple', 'banana', 'cherry']
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [72], in <cell line: 3>()
          1 mylist = thislist.copy()
          2 print(mylist)
    ----> 3 a = list([1])
          4 print(a)
    

    TypeError: 'list' object is not callable



```python
mylist[0] = 1
print(mylist)
```

    [1, 'banana', 'cherry']
    


```python
print(thislist)
```

    ['apple', 'banana', 'cherry']
    


```python
# Make a copy of a list with the list() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
```

    ['apple', 'banana', 'cherry']
    


```python
# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
```

    ['a', 'b', 'c', 1, 2, 3]
    


```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)
```

    ['a', 'b', 'c', 1, 2, 3]
    


```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

list1.append(list2)
print(list1)
```

    ['a', 'b', 'c', 1, 2, 3]
    ['a', 'b', 'c', 1, 2, 3, [1, 2, 3]]
    


```python

```

### Tuple


```python
# Create a Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```

    ('apple', 'banana', 'cherry')
    


```python
# Tuple items are ordered, unchangeable, and allow duplicate values.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
```

    ('apple', 'banana', 'cherry', 'apple', 'cherry')
    


```python
# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
```

    3
    


```python
# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = "apple"
print(type(thistuple))
```

    <class 'tuple'>
    <class 'str'>
    


```python
thistuple = ("apple",)
print(type(thistuple))
print(thistuple)

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
print(thistuple)
```

    <class 'tuple'>
    ('apple',)
    <class 'str'>
    apple
    


```python
 # Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
```


```python
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
```

    ('abc', 34, True, 40, 'male')
    


```python
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
```

    <class 'tuple'>
    


```python
# tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
```

    ('apple', 'banana', 'cherry')
    


```python
# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
```

    banana
    


```python
# Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
```

    cherry
    


```python
# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
```

    ('cherry', 'orange', 'kiwi')
    


```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
```

    ('apple', 'banana', 'cherry', 'orange')
    


```python
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
```

    ('cherry', 'orange', 'kiwi', 'melon', 'mango')
    


```python
# Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
```

    ('orange', 'kiwi', 'melon')
    


```python
# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
```

    Yes, 'apple' is in the fruits tuple
    


```python
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
x = ("apple", "banana", "cherry")
x[0] = 'kiwi'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [95], in <cell line: 3>()
          1 # Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
          2 x = ("apple", "banana", "cherry")
    ----> 3 x[0] = 'kiwi'
    

    TypeError: 'tuple' object does not support item assignment



```python
# Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [96], in <cell line: 3>()
          1 # Change Tuple Values
          2 x = ("apple", "banana", "cherry")
    ----> 3 y = list(x)
          4 y[1] = "kiwi"
          5 x = tuple(y)
    

    TypeError: 'list' object is not callable



```python
# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [97], in <cell line: 3>()
          1 # Add Items
          2 thistuple = ("apple", "banana", "cherry")
    ----> 3 y = list(thistuple)
          4 y.append("orange")
          5 thistuple = tuple(y)
    

    TypeError: 'list' object is not callable



```python
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
```

    ('apple', 'banana', 'cherry', 'orange')
    


```python
# Remove Items 
thistuple = ("apple", "banana", "cherry") 
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [99], in <cell line: 3>()
          1 # Remove Items 
          2 thistuple = ("apple", "banana", "cherry") 
    ----> 3 y = list(thistuple)
          4 y.remove("apple")
          5 thistuple = tuple(y)
    

    TypeError: 'list' object is not callable



```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
del thistuple
print(thistuple)
```

    ('apple', 'banana', 'cherry')
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [100], in <cell line: 4>()
          2 print(thistuple)
          3 del thistuple
    ----> 4 print(thistuple)
    

    NameError: name 'thistuple' is not defined



```python
# Unpack Tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
```

    apple
    banana
    cherry
    


```python
# Using Asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(type(red))
print(red)
```

    apple
    banana
    <class 'list'>
    ['cherry', 'strawberry', 'raspberry']
    


```python
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
```

    apple
    ['mango', 'papaya', 'pineapple']
    cherry
    


```python
# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
```

    apple
    banana
    cherry
    


```python
# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
```

    apple
    banana
    cherry
    


```python
# Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
```

    apple
    banana
    cherry
    


```python
# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```

    ('a', 'b', 'c', 1, 2, 3)
    


```python
# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
```

    ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
    


```python

```
