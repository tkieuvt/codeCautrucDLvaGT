n = int(input("n = "))
print("SNT tu 1 den", n, "là:")
for num in range(2, n + 1):
    SNT = True
    for i in range(2, num):
        if num % i == 0:
            SNT = False
            break
    if SNT:
        print(num, end=' ')