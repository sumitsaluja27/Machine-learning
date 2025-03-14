name = "Sumit" #this is a string. String is data type which is a sequence of character.
# once string is created then it can not be changed
# string slicing. It can be done by indexing. Any word can be index. Indexing starts with letter 0(zero) or it can go
# from reverse as well where it start with -1(minus one). 
# In the above exmaple s(can be 0 or -5) u(can be 1 or -4) m(can be 2 or -3) i(can be 3 or -2) t(can be 4 or -1)
nameshort = name[0:3]  #in this case from 0 to 2 shall get included
# in this case sum will be reflected. Below is the print program
print(nameshort)
# If we need only one character
character1 = name[0]
print(character1)

# skip value. This is quite interesting. For example below; we want every second word till 6th word and we need to skip 2 word. Let us explain more
# a(0), m(1), a(2), z(3), i(4), n(5) and g(6). in this case, 1st which is m is starting point, taken till n(5) becauese 6 is not included
# and every 2nd word is taken. So m(1), then skip m and a(2 words), then z and i and skipped and n is included. so MZN is the output.
word = "amazing"
slice = word[1:6:2]
print(slice)


