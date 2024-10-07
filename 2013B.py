R = lambda : map(int,input().strip().split())
def Testcases():
    n, = R()
    a = list(R())
    print(sum(a[:n-2]) - a[n-2] + a[n-1])
    pass
for _ in range(int(input())):
    Testcases()
