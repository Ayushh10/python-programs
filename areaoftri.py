import math
a=int(input("enter side A"))
b=int(input("enetr side B"))
c=int(input("enetr side C"))
P=a+b+c
s=(a+b+c)/2
A=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Perimeter is:", P)
print("area of triangle is:", A)
