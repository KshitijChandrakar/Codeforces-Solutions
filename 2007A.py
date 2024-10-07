R = lambda : map(int,input().strip().split())
def Testcases():
    l,r = R()
    print(r-l+l%2+1>>2)
    pass
for _ in range(int(input())):
    Testcases()
