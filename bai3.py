import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
denta=b*b-4*a*c
if denta>0:
    x1=((-b+math.sqrt(denta))/(2*a))
    x2=((-b-math.sqrt(denta))/(2*a))
    print("x1=",x1,"\nx2=",x2)
elif denta==0:
    x=-b/(2*a)
    print("x1=x2=",x)
else:
    print("Phuong trinh vo nghiem")
    
    
    
    
    
    
    
        
