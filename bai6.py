n=int(input("So luong phan tu: "))
L=[]
for i in range(n):
    x=int(input())
    L.append(x)
max=L[0]
for x in L:
    if x>max: max=x
print("Phan tu lon nhat trong day:",max)