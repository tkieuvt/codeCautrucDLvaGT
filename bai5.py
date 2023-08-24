import math
def sohoanhao(x):
    s = 0 
    for i in range(1,int(x/2)+1):
        if x % i == 0 : s += i
    if s == x : print(x)
n = int(input())
for i in range(2,n+1):
    sohoanhao(i)