a = input("enter number 1: ")

b = input("enter number 2: ")

print("number a is:", a)
print("number a is:", b)
# print("Sum is", a + b)
# now the result is 12 because a and b are str not the integer.
# to get the right result we either have to convert them in integer by using type or type integer itself
# below is more explanation with example
a = int(a)
b = int(b) #here I have converted them in integer and now the result shall be different
print("sum is ", a+b)


