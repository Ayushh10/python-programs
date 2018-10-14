import math
print("for quadratic equations , ax**2+bx++c=0, enter coefficient below")
a=int(input("Enter a:"))
b=int(input("Enetr b:"))
c=int(input("Enter c:"))
if a==0:
 print("value of", a,'should be zero')
 print("\n aborting!!!")
else:
 delta= b*b -4*a*c
if delta > 0:
    root1=( -b+ math.sqrt(delta))/(2*a)
    root2=( -b- math.sqrt(delta))/(2*a)
    print("roots are REAL and UNEQUAL")
    print("root1=",root,",root2=",root2)
elif delta==0:
    root1= -b/(2*a);
    print=("roots are REAL and EQUAL")
    print=("root1=",root1,",root2=",root2)
else:
    print("roots are COMPLEX and IMAGINARY")
