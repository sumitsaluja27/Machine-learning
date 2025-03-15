"""
📌 Python Learning Notes - Chapter 1: Introduction to Python

Author: Sumit Saluja
Date: [15th-March-2025]
Description: This file contains structured notes and explanations of key Python concepts 
covered in Chapter 1. It serves as a learning guide for beginners.

---
"""

# ===============================================
# 📝 1. Introduction to Python
# ===============================================
"""
Python is a high-level, interpreted programming language known for its readability 
and ease of use. It is widely used in web development, machine learning, automation, 
and data science.

🔹 Features of Python:
✔ Easy to Learn and Use
✔ Open Source and Free
✔ Cross-platform Compatibility
✔ Supports Object-Oriented Programming (OOP)
✔ Rich Standard Library

"""
# we put # in front of a sentence if we want to provide our comments. Like a sentence to explain something.


# 1st PROGRAM
# to get any output we always type: PRINT(....). for example if we want to write Hello, how are you? we will write print(Hello, how are you?)


# module = module is a file that contains a code for specific job
# packages = packages contains modules to built bigger application. Pandas, numbpy, pytest etc is an example of packages
# libraries = libraries contains a lot of modules and packages. pytorch and tensorflow are the examples
# framework = Similar to libraries, Python frameworks are a collection of modules and packages that help programmers to 
# fast track the development process. However, frameworks are usually more complex than libraries. 
# Also, while libraries contain packages that perform specific operations, frameworks contain the basic flow and architecture of the application.

# 

# ===============================================
# 🔤 2. Variables and Data Types
# ===============================================
#Variables= Variables are set of containers in which data is stored. In below written text x, name, pi, is_python_fun are variables.
# Data= Data is the value that variable contains. For example 10, "sumit", 3.14 and true are data.
# imp things about variables and data
# VARIABLES:
# a) cant have space in between so we use _ 
# b) Always avoid special characters like #,$,%,^, ! etc.
# c) variables are lower and upper case sensitive. For example if we use age is not Age because one has lower case and upper case.
# d) make sure variables have meaning

# DATA TYPE: there are 7 types of data which are below:
# a)string (denoted as str)= It is text and it has to start with "" (double quote). for example name = "sumit".
# b)integer (denoted as int)= these are whole numbers like 1, 2, 3, 4 etc
# c)flot = these always have a digit. in below example pi is a variable and 3.14 is a floating data
# d)boolean(pronounced as boo-li-an) it is alwawya denote as true or false
# e)list = it is collection of things. For example fruits = ["apple", "banana", "cherry"]. Always use [ ] in list and tuples. 
# You will study why later on.
# f) tuple = tuple is also ike like list but this can not be changed. For example cordinates (10, 20). It is called as immutable.

# DATA TYPE IS IMPORTANT TO MAKE PYTHON UNDERSTAND YOU ARE DOING AND WHAT YOU ARE REFERING TO.

# ✅ Variable Declaration
x = 10      # Integer
name = "Sumit"  # String
pi = 3.14   # Float
is_python_fun = True  # Boolean

# 🔹 Data Type Checking
print(type(x))        # <class 'int'>
print(type(name))     # <class 'str'>
print(type(pi))       # <class 'float'>
print(type(is_python_fun))  # <class 'bool'>

"""
🔹 Notes:
- Variables store data and can be reassigned.
- Python is **dynamically typed**, meaning you don’t need to define variable types explicitly.
"""

# ===============================================
# ➗ 3. Basic Arithmetic Operators
# ===============================================

# Addition, Subtraction, Multiplication, Division
a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division (floating-point): 3.333

"""
🔹 Notes:
- `/` always returns a float.
- `//` is floor division, rounding down the result.
- `**` is the exponentiation operator (power).
"""

# ===============================================
# 🔄 4. Control Flow (if-else, loops)
# ===============================================

# ✅ If-Else Statement
age = 18

if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor.")

"""
🔹 Notes:
- Indentation is crucial in Python (4 spaces per level).
- `if`, `elif`, and `else` control program decisions.
"""

# ✅ Loops (for & while)
# 🔹 For Loop Example
for i in range(5):
    print(f"Iteration {i}")

# 🔹 While Loop Example
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

"""
🔹 Notes:
- `for` loops iterate over a sequence (list, range, etc.).
- `while` loops run as long as a condition is `True`.
"""

# ===============================================
# 📦 5. Modules and Importing
# ===============================================

# Importing a built-in module
import math

print(math.sqrt(25))  # Output: 5.0

"""
🔹 Notes:
- Modules are Python files that contain functions and variables.
- Built-in modules include `math`, `random`, `os`, etc.
- Custom modules can be created and imported.
"""

# ===============================================
# 🏁 6. Summary and Next Steps
# ===============================================

"""
✅ Summary:
- Learned how to write program with print
- Learned about Python variables and data types.
- Explored module, library, packages and.
- Used if-else conditions and loops.
- Imported and used built-in modules.
- basic arithematic operartions
- how to check data type

🚀 Next Steps:
In Chapter 2, we will dive deep into these topics.

🎯 Keep practicing and experimenting with Python code!
"""
