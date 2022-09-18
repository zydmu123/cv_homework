<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"></ul></div>

# First Python Code


```python
print('Hello World')
```

    Hello World
    


```python
students_count = 1000
print(students_count)
print(id(students_count))

```

    1000
    2120909552592
    


```python
students_count = students_count + 4
print(students_count)
```

    1004
    


```python
students_count = "Python Programming"
print(students_count)
print(id(students_count))
```

    Python Programming
    2120385297904
    


```python

```


```python
print('I'm Jian Zhang')
```


      Input In [5]
        print('I'm Jian Zhang')
                 ^
    SyntaxError: invalid syntax
    



```python
print("I'm Jian Zhang")
```

    I'm Jian Zhang
    


```python
print('''I'm 
Jian Zhang
'''
)
```

    I'm 
    Jian Zhang
    
    

# Line by line


```python
print('o----')
print(' ||||')
print(5 * 10)
print('*' * 10)
```

    o----
     ||||
    50
    **********
    

# Variable 


```python
price = 10
```


```python
print(price)

price = 20

print(id(price))

price = price + 2

print(id(price))
```

    10
    140721195065696
    140721195065760
    


```python
rating = 4.9
```


```python
name = 'Jack'
```


```python
is_true = True
```


```python
print(type(rating))

print(type(is_true))

print(type(name))
```

    <class 'float'>
    <class 'bool'>
    <class 'str'>
    


```python
students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print(type(students_count))
print(type(rating))
print(type(is_published))
print(type(course_name))
print(id(rating))
print(id(students_count ))

```

    <class 'int'>
    <class 'float'>
    <class 'bool'>
    <class 'str'>
    2120909553232
    2120909553392
    

# Patient Example: Name, age


```python
name = input('What is your name? ')
print('Hi ' + name)
```

    What is your name? xy
    Hi xy
    


```python
name = input('What is your name? ')
age = input('What is your age? ')
print(name + ' is ' + age + ' years old.')
```

    What is your name? ET 120
    What is your age? 120
    ET 120 is 120 years old.
    


```python
price = 1_000_000
```


```python
print(price)
```

    1000000
    


```python
print(type(price))
```

    <class 'int'>
    

# Formatted String


```python
first_name = "Jian"
last_name = "Zhang"
full_name = first_name + " " + last_name
print(full_name)
full_name_formated = f"{first_name} {last_name}"
print(full_name_formated)
```

    Jian Zhang
    Jian Zhang
    

# Escape Character


```python
course_full_name = "Python Programing with \"Mosh\""
print(course_full_name)
course_full_name = "Python Programing with \'Mosh\'"
print(course_full_name)
course_full_name = "Python Programing with \\Mosh\\"
print(course_full_name)
course_full_name = "Python Programing with \nMosh"
print(course_full_name)
```

    Python Programing with "Mosh"
    Python Programing with 'Mosh'
    Python Programing with \Mosh\
    Python Programing with 
    Mosh
    

# String Methods


```python
course_name_python = "  python programming for beginners    "
print(course_name_python.upper())
print(course_name_python.lower())
print(course_name_python.title()) 
print(course_name_python.find("gram"))
print(course_name_python.replace("p", "P"))
print("pro" in course_name_python)
print("abc" in course_name_python)
```

      PYTHON PROGRAMMING FOR BEGINNERS    
      python programming for beginners    
      Python Programming For Beginners    
    12
      Python Programming for beginners    
    True
    False
    

# Numbers


```python
x = 3
y = 3.1
z = 3 + 2j  
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  #round down the integer in the quotient
print(10 % 3)
print(10 ** 3)
x = x + 3
print(x)
y += 3
print(y)
print(z)

```

    13
    7
    30
    3.3333333333333335
    3
    1
    1000
    6
    6.1
    (3+2j)
    


```python
print(type(z))
```

    <class 'complex'>
    


```python
# Working with Numbers
```


```python

import math
print(round(2.9595, 2))  # Function to round numbers
print(abs(-5.4))        # Converts a number to absolute
print(math.ceil(8.2))   # Math function to retunr the ceil of a float number
print(math.floor(4.9))

average = 2.9
print(f"{average:.2f}")
```

    2.96
    5.4
    9
    4
    2.90
    

# Type Conversion


```python
# 09 Type Conversion
x = input("x: ")  # Even if the input is a number it will be read as a string
print(type(x))

y = int(x) + 5
print(f"x: {x} ; y: {y}")

# type converters
# int() converts to an interger

# float() converts to float

# bool() converts to boolean
# Falsy values - values that retunr False
print(bool(""))  # Double quotations returns False  ----zzy
print(bool(0))  # 0 returns False
print(bool(None))
# Other values return True
print(bool(2))
# str() converts to string
```

    x: 2
    <class 'str'>
    x: 2 ; y: 7
    False
    False
    False
    True
    

# Quiz


```python
# 10 Quiz

# What are the primitive type in python?
# Strings
# Interger number
# Float numbers
# Booleans - True and False

# What will we see in the terminal
fruit = "Apple"
print(fruit[1])
# p

# What will we see in the terminal?
fruit = "Apple"
# when slicing a string the last caracter called is not inclued
print(fruit[1:-1])
# ppl

# Waht is the result?
print(10 % 3)
# 1

# Whats the result?
print(bool("False"))
# True
```

    p
    ppl
    1
    True
    

# Comparison operators


```python
# 01 Comparison operators

# Use comparison operator to compare values
# < strictly less than
# <= less than or equal
# > strictly greater than
# >= greater than or equal
# == equal
# != not equal
# is object identity
# is not negated object identity
```


```python
print(3>2)
```

    True
    


```python
print(3<2)
```

    False
    

# Conditional Statements


```python
# 02 Conditional Statements

temperature = 25
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")
```

    It's nice
    Done
    

# Ternary Operator


```python
age1 = 17
if age1 >= 18:
    print("Eligible")
else:
    print("Not eligible")

# Theres is a different cleaner way to write the same code, and achive the same result.
age2 = 20
message = "Eligible" if age2 >= 18 else "Not eligible"
print(message)
```

    Not eligible
    Eligible
    

# Logical Operators


```python
# 04 Logical Operators
# and
# or
# not

income = 2000
good_credit = True

if income > 2500:
    high_income = True
    print("You have a high income!")
else:
    high_income = False
    print("You have a low income")

if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

income = 2000
good_credit = True

if income > 2500:
    high_income = True
    print("You have a high income!")
else:
    high_income = False
    print("You have a low income")

if high_income or good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


```

    You have a low income
    Not eligible for loan
    You have a low income
    Eligible for loan
    


```python
income = 2000
good_credit = True
student = False

if income > 2500:
    high_income = True
    print("You have a high income!")
else:
    high_income = False
    print("You have a low income")

if not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


income = 5000
good_credit = True
student = True

if income > 2500:
    high_income = True
    print("You have a high income!")
else:
    high_income = False
    print("You have a low income")

if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
```

    You have a low income
    Eligible for loan
    You have a high income!
    Not eligible for loan
    

# Chaining Comparison Operators


```python
# age should be between 18 and 65

age = 22

if age >= 18 and age < 65:
    print("Eligible")

if 18 <= age < 65:
    print("Eligible")

# Line 7 and line 10 are the exact same code
```

    Eligible
    Eligible
    

# For Loops


```python
# 08 For Loops

# They are used to reapet a task
# In this example we are trying to send a message to a use at least 3 time

for number in range(3):  # the range goes from 0, 1, 2
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):  # range goes from 1, 2, 3
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):  # range goes from 1, 3, 5, 7, 9
    print("Attempt", number, number * ".")
```

    Attempt 1 .
    Attempt 2 ..
    Attempt 3 ...
    Attempt 1 .
    Attempt 2 ..
    Attempt 3 ...
    Attempt 1 .
    Attempt 3 ...
    Attempt 5 .....
    Attempt 7 .......
    Attempt 9 .........
    

# For..Else


```python
# Lesson how to break a for loop

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
```

    Attempt
    Attempt
    Attempt
    Attempted 3 times and failed
    

# Iterables


```python
# 11 Iterables

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)
```

    P
    y
    t
    h
    o
    n
    1
    2
    3
    4
    

# Nested Loops


```python
# 10 Nested Loops
# Loops inside other loops

for x in range(2):
    for y in range(3):
        print(f"({x},{y})")
```

    (0,0)
    (0,1)
    (0,2)
    (1,0)
    (1,1)
    (1,2)
    

# While Loops


```python
# 12 While Loops

number = 100
while number > 0:
    print(number)
    number = number // 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("Echo", command)
```

    100
    50
    25
    12
    6
    3
    1
    >we
    Echo we
    >qq
    Echo qq
    >quit
    Echo quit
    

# Infinite Loops


```python
# 13 Infinite Loops

while True:
    command = input(">")
    print("Echo", command)
    if command.lower() == "quit":
        break
```

    >we
    Echo we
    >quit
    Echo quit
    


```python

```


```python
# 11 Exercise

# Display the even number ( 2 4 6 8) followed by this message "We have 4 even numbers"
# 2
# 4
# 6
# 8
# We have 4 even numbers

# My anwser
for number_even in range(1, 10):
    if number_even % 2 == 0:
        print(number_even)
    elif number_even > 8:
        print("We have 4 even numbers")
        break

# Mosh anwser
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count = count + 1
        print(number)
print(f"we have {count} even number")


# In my anwser I did not count the numbers


# zzy's answer
for num in range(1,10):
    if num % 2 != 0:
        continue
    else:
        print(num)
    if num>=8:
        print("We have 4 even numbers")
        break      

```

    2
    4
    6
    8
    We have 4 even numbers
    2
    4
    6
    8
    we have 4 even number
    2
    4
    6
    8
    We have 4 even numbers
    


```python

```


```python

```


```python

```


```python

```


```python
for
    for 
```


```python

```


```python

```


```python

```


```python

```
