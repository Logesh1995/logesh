# 1. Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included).
a= 2000
b= 3200
while a<=b:
    if a%7==0 and a%5!=0:
        print(a, end=',')
    a= a+1