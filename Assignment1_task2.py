# 2. Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name.
a = input("Enter ur first name:")
b= input ('Enter ur last name:')

c= len(a)
d= len(b)

for i in range(1,c+1):
    print(a[-i], end='')
print(" ", end='')
for j in range (1,d+1):
    print(b[-j], end='')