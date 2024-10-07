R = lambda : map(int,input().strip().split())
def Testcases():
    l,r = R()
    n = 0
    while True:
        if l + (2+(n-1))*n/2 > r:
            break
        else:
            n+= 1
    print(n)
    pass
for _ in range(int(input())):
    Testcases()
