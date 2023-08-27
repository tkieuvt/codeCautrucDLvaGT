import math
a1 = int(input("a1 = "))
b1 = int(input("b1 = "))
a2 = int(input("a2 = "))
b2 = int(input("b2 = "))
print("tu la:",int((a1*b2+a2*b1)/math.gcd(a1*b2+a2*b1,b1*b2)))
print("mau la:",int((b1*b2)/math.gcd(a1*b2+a2*b1,b1*b2)))