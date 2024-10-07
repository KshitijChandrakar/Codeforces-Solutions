# Math Approach
R = lambda : map(int,input().strip().split())

def Testcases():
    l,r = R()
    n = (2 * (r-l) + 2)**(0.5)
    print(round(n))
    pass
for _ in range(int(input())):
    Testcases()
