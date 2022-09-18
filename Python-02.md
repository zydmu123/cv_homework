<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"></ul></div>


```python
import math

a = 0.36
b = math.sqrt(a)
print(b)
```

    0.6
    


```python

```


```python
from MyQR import myqr


# """Generate a QR code"""
myqr.run(words='https://villa.jianzhang.tech/',
         save_name='01.png',
         )

# """Generate a QR code with a background picture"""
# myqr.run(words='https://villa.jianzhang.tech/',
#          picture=r'duola.jpg',
#          colorized=True,   # True：Color，False：Gray
#          save_name='002.png')
```

    line 16: mode: byte
    




    (4,
     'H',
     'C:\\Users\\nudtzzy\\Desktop\\workplace\\4PeK-课件等\\03-计算机视觉\\2022-PKUSZ-CV-课件\\2022计算机视觉-第2周\\01.png')




```python
# Functions
```


```python
def my_function():
    print("Hello from a function")
```


```python
my_function()
```

    Hello from a function
    


```python
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
```

    Emil Refsnes
    Tobias Refsnes
    Linus Refsnes
    


```python
def add(a,b):
    return a+b
```


```python
def lessthan(a,b):
    return a<=b
```


```python
print(add(5,4))
```

    9
    


```python
print(lessthan(5,4))
```

    False
    


```python

```


```python
# 01 Lists

# Example of a list with strings
letters = ["a", "b", "c"]
print(letters)

# Exemple of a list with interger
numbers = [1, 2, 3, 4]
print(numbers)
```

    ['a', 'b', 'c']
    [1, 2, 3, 4]
    


```python
# Each item in this list is a list it self.
matrix = [[0, 1], [2, 3]]
print(matrix)

# Example how to create list
zeros = [0] * 5
print(zeros)
```

    [[0, 1], [2, 3]]
    [0, 0, 0, 0, 0]
    


```python
# Concatenate lists
combined = zeros + letters
print(combined)

# Creat a list of a sequence of numbers, in this example from 5 to 20
list_range = list(range(5, 21))
print(list_range)
```

    [0, 0, 0, 0, 0, 'a', 'b', 'c']
    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    


```python
# Convert a string to a list
string_list = list("Python")
print(string_list)

# Check the number of item in a list
item_in_string_list = len(string_list)
print(item_in_string_list)
```

    ['P', 'y', 't', 'h', 'o', 'n']
    6
    


```python
# 02 Accessing Items

#  a   b   c   d - example list
#  0   1   2   3 - position of each item in the list 
# -4  -3  -2  -1 - or position of the item ins reverse
letters = ["a", "b", "c", "d"]
print(letters)

first_item = letters[0]  # to access the item number 0 in the list
print(first_item)

letters[0] = "A"  # to change the first item in the list

print(letters)

numbers = list(range(20))
print(numbers)
```

    ['a', 'b', 'c', 'd']
    a
    ['A', 'b', 'c', 'd']
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    


```python
# Like string this is to slice a list [first item : last item: step] all arguments are optinal
numbers_slice = numbers[2:15:2]
print(numbers_slice)

# with this we are able to reverse the order of the list
numbers_revers = numbers[::-1]
print(numbers_revers)
```

    [2, 4, 6, 8, 10, 12, 14]
    [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    


```python
# 03 List Unpacking

numbers = [1, 2, 3]
print(numbers)

# Assigning an item of a list to a variable
# first = numbers[0]
# second = numbers[1]
# third = numbers[3]
```

    [1, 2, 3]
    


```python
# The best way to this is by list unpacking
first, second, third = numbers
print(first)
print(second)
print(third)
```

    1
    2
    3
    


```python
# If we have alist with a lot of item and we just want to unpack the first two item and pack the rest of item in another list
numbers_0_19 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(numbers_0_19)
first, second, *others = numbers_0_19
print(first)
print(second)
print(others)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    0
    1
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    


```python
# For example if we want the unpack the first and the the last item
first, *others, last = numbers_0_19
print(first)
print(others)
print(last)
```

    0
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    19
    


```python
# 04 Looping over Lists

letters = ["a", "b", "c", "d"]

for letter in letters:
    print(letter)

```

    a
    b
    c
    d
    


```python
# to get the index of each item use the built in function enumerate()
for letter in enumerate(letters):
    print(letter)
```

    (0, 'a')
    (1, 'b')
    (2, 'c')
    (3, 'd')
    


```python
for index, letter in enumerate(letters):
    print(index, letter)
```

    0 a
    1 b
    2 c
    3 d
    


```python
# 05 Adding or Removing Items

letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)

# Add an item to the end of the list
letters.append("h")
print(letters)
```

    ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    


```python
letters.insert(2, "-")
print(letters)
```

    ['a', 'b', '-', 'c', 'd', 'e', 'f', 'g', 'h']
    


```python
# Remove an item of a list use the method pop()
# with no argument it removes the last item
letters.pop()
print(letters)
```

    ['a', 'b', '-', 'c', 'd', 'e', 'f', 'g']
    


```python
# with a argument it removes the item with that index
letters.pop(2)
print(letters)
```

    ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    


```python
# Remove an item for a list using the method remove()
# specify the item
letters.remove("c")  # this will remove the first "c" in the list
print(letters)
```

    ['a', 'b', 'd', 'e', 'f', 'g']
    


```python
letters.append("e")
```


```python
print(letters)
```

    ['a', 'b', 'd', 'e', 'f', 'g', 'e']
    


```python
letters.remove("e")  # this will remove the first "c" in the list
print(letters)
```

    ['a', 'b', 'd', 'f', 'g', 'e']
    


```python
# Remove item using the del statement
# with this statement we can remove one item or a range of items by the index
del letters[0:2]
print(letters)
```


```python
# to clear the list and delete all the items
letters.clear()
print(letters)
```

    []
    


```python
# 06 Finding Items

letters = ["a", "b", "c", "d", "e", "f", "g"]

print(letters.index("d"))
```

    3
    


```python
print(letters.index("h"))
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Input In [32], in <cell line: 1>()
    ----> 1 print(letters.index("h"))
    

    ValueError: 'h' is not in list



```python
# Example 1
if "d" in letters:
    print(letters.index("d"))

# Exemple 2
print(letters.count("m"))
```

    3
    0
    


```python
# 07 Sorting Lists

numbers = [5, 51, 2, 15, 6]
print(numbers)

# sort numbers with the sort() method
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

```

    [5, 51, 2, 15, 6]
    [2, 5, 6, 15, 51]
    [51, 15, 6, 5, 2]
    


```python
numbers = [5, 51, 2, 15, 6]
print(numbers)
# The sort function can be used an it will creat a new list
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)
```

    [5, 51, 2, 15, 6]
    [2, 5, 6, 15, 51]
    [51, 15, 6, 5, 2]
    [5, 51, 2, 15, 6]
    


```python
# Zip Function
list_1 = [1, 2, 3, 4]
list_2 = [10, 20, 30, 40, 50, 60]

combined_list = zip(list_1, list_2)
print(list(combined_list))

list_3 = list(zip("abcd", list_2, list_1))
print(list_3)
```

    [(1, 10), (2, 20), (3, 30), (4, 40)]
    [('a', 10, 1), ('b', 20, 2), ('c', 30, 3), ('d', 40, 4)]
    


```python
# Swapping Variables

# To swap two variables, we can use a third variable to backup the frist variable

x = 10
y = 20

# z = x
# x = y
# y = z

print(f"x: {x}\ny: {y}")

# In python we can swap the value of two variables using only one line of code
x, y = y, x

print(f"x: {x}\ny: {y}")
```

    x: 10
    y: 20
    x: 20
    y: 10
    


```python
# Sets

numbers = [1, 1, 2, 5, 4, 5, 1, 2, 2, 1, 4, 5, 5]
uniques = set(numbers)
print(uniques)

# We can use the same methods as lists
uniques.add(6)
print(uniques)

uniques.remove(6)
print(uniques)

print(len(uniques))
```

    {1, 2, 4, 5}
    {1, 2, 4, 5, 6}
    {1, 2, 4, 5}
    4
    


```python
a = set()
print(a)
a.add('b')
print(a)
```

    set()
    {'b'}
    


```python
# Tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)
```

    ('apple', 'banana', 'cherry')
    


```python
print(thistuple[0])
```

    apple
    


```python
print(thistuple[0:2])
```

    ('apple', 'banana')
    


```python
thistuple[0] = 'orange'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [48], in <cell line: 1>()
    ----> 1 thistuple[0] = 'orange'
    

    TypeError: 'tuple' object does not support item assignment



```python
# List Comprehensions

products = [
    ("Product1", 15),
    ("Product2", 50),
    ("Product3", 5)
]
print(products)

prices = [item[1] for item in products] 
print(prices)
```

    [('Product1', 15), ('Product2', 50), ('Product3', 5)]
    [15, 50, 5]
    


```python
filtered_price = [item for item in products if item[1] >= 10]
print(filtered_price)
```

    [('Product1', 15), ('Product2', 50)]
    


```python
# Dictionaries

point = {"x": 1, "y": 2}
print(point)
point = dict(x=1, y=2)
print(point)
```

    {'x': 1, 'y': 2}
    {'x': 1, 'y': 2}
    


```python
print(point["x"]) 
```

    1
    


```python
point["z"] = 3
print(point)
```

    {'x': 1, 'y': 2, 'z': 3}
    


```python
if "a" in point:
    print("yes")
else:
    print("no")
```

    no
    


```python
print(point.get("a"))
```

    None
    


```python
del point["x"] # to delete the key x
print(point)
```

    {'y': 2, 'z': 3}
    


```python
for key in point: # Loop over dictoanaries, in here we will print the dictionary keys
    print(key)
```

    y
    z
    


```python
for key in point: # Loop over 
    print(key, point[key])
```

    y 2
    z 3
    


```python
for index in point.items(): 
    print(index)
```

    ('y', 2)
    ('z', 3)
    


```python
for key, value in point.items():
    print(key, value)
```

    y 2
    z 3
    


```python
print(point.items())
print(list(point.items()))
print(tuple(point.values()))
```

    dict_items([('y', 2), ('z', 3)])
    [('y', 2), ('z', 3)]
    (2, 3)
    


```python
# Dictionary Comprehensions
valores = {x: x * 2 for x in range(5)}
print(valores)
```

    {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
    


```python
from sys import getsizeof # import getsizeof function
print(getsizeof(valores)) # show the bites of memory
```

    232
    


```python
a = 3
print(getsizeof(a))
```

    28
    


```python
# Unpacking Operator

numbers = [1, 2, 3]
print(numbers)
print(*numbers) # with * operator we are unpacking the list and passing them as single elements to the print function
```

    [1, 2, 3]
    1 2 3
    


```python
print((*numbers))
```

    1 2 3
    


```python
values = list((range(10)))
print(values)
values  = [*range(10)] # With this operator we can unpack any iterables
print(values)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    


```python
my_text = [*"Hello Miguel"]
print(my_text)
```

    ['H', 'e', 'l', 'l', 'o', ' ', 'M', 'i', 'g', 'u', 'e', 'l']
    


```python
# We can combine multiple list
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
combined_lists = [*list_1, *list_2]
print(combined_lists)

```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    


```python
# We can also unpack dictonaries but we have to use **

dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 4, "c": 6}
combined_dict = {**dict_1, **dict_2} 
print(combined_dict)
```

    {'a': 1, 'b': 4, 'c': 6}
    


```python

```
