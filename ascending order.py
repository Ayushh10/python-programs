x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))
if x<y and x<z:
    if y<z:
        min,mid,max=x,y,z
    else:
        min,mid,max=x,z,y
elif y<x and y<z:
    if x<z:
        min,mid,max=y,x,z
    else:
        min,mid,max=y,z,x
else:
    if x<y:
        min,mid,max=z,x,y
    else:
        min,mid,max=z,y,x
print("Numbers in ascending order are : ",min,mid,max)
