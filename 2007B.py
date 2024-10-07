R = lambda : map(str,input().strip().split())
R1 = lambda : map(int,input().strip().split())
def Testcases():
    n,m = R1()
    A = list(R1())
    A = max(A)
    for i in range(m):
        o,l,r = R()
        A += l<=A<=r and 44-ord(o)
        print(A, end = " ")
    print()

for _ in range(int(input())):
    Testcases()
