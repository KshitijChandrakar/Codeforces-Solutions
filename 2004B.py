def intersection(l1, r1, l2, r2):
    start = max(l1, l2)
    end = min(r1, r2)
    return (start, end) if start<=end else 0
R = lambda : map(int,input().strip().split())
IN = lambda a,b,c: b<=a<=c
def Testcases():
    l,r = R()
    p,q = R()
    if r-l < q-p:
        l,r,p,q =p,q,l,r

    print(l,r,p,q)
    z = intersection(l,r,p,q)
    offset = 0
    if z == 0:
        print(1)
        return
    diff = z[1] - z[0]
    if IN(z[0],l,r) or z[0] != l:
        print("a")
        offset += 1
    if IN(z[1], p, q) or z[1] != q:
        print("b")
        offset += 1
    print(z, offset)
    print(offset + z[1] - z[0] if z != 0 else 1)
    pass
for _ in range(int(input())):
    Testcases()
