import math
def sohoanhao(x):
    s = 0 
    for i in range(1,int(x/2)+1):
        if x % i == 0 : s += i
    if s == x : print(x,end=' ')
n = int(input("n = "))
print("So hoan hao tu 1 den", n, "là:")
for i in range(2,n+1):
    sohoanhao(i)