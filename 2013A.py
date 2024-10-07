R = lambda : map(int,input().strip().split())
ru = lambda z : int(int(z) + 1) if int(z) < z else int(z)
def Testcases():
    n, = R()
    x,y = list(R())
    print(ru(n/min(x,y)))
    pass
for _ in range(int(input())):
    Testcases()
