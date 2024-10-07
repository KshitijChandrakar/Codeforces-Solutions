R = lambda : map(int,input().strip().split())
ru = lambda z : int(z) + 1 if int(z) < z else int(z)


def Testcases():
    a,b = 0,0
    a,b = R()
    print("YNEOS"[a%2or a<1 and b%2::2])
for _ in range(int(input())):
    Testcases()
