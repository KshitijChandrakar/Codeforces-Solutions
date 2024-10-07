R = lambda : map(int,input().strip().split())
def Testcases():
    n, = R()
    a = list(R())
    if n < 2:
        print(1 + a[0])
        return
    b = a[1::2]
    a = a[0::2]
    maxA = max(a)
    maxB = max(b)
    maxC = max(maxA + len(a),maxB + len(b))
    print(maxC)
    pass
for _ in range(int(input())):
    Testcases()
