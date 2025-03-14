# (there are 4 operators primarily
# 1. Arithematic operators: +, -, *, / etc
# 2. Assignment operators: =, +=, -= etc
# 3. comparison operator: ==, >, >=, <, != etc
# 4. Logical operators: and, or, not
# for example 7+4=11 in this 7 and 4 are operands and + is an operator
# )
# Arithmetic operators
a = 4
b = 5
c = a + b
print(c)

# assignment operators
a = 4-2 
b = 6
# b += 4 # this means increment the value of b and assign it to b
print(b)
# b -=1
b *=4
print(b)

# comparison operators
d = 5<4
print(d) # comparison operators are always booolean data
d = 2!=7 # to show not equal to we use !=. meaning of "!" is not whenever we code
print(d)

# logical operators
e = True or False
print(e)
# truth table of or
print("true or false is", True or False)
print("true or true is", True or True)
print("false or true", False or True)
print("false or false is", False or False)

# truth table of and
print("true and false is", True and False)
print("true and true is", True and True)
print("false and true", False and True)
print("false and false is", False and False)
# so, the differnce between or & and operators is that in 'or' we need both false to be false & in and we need both true to be true

# not only operates on one operand. it makes true as false and false as true
print(not(False))