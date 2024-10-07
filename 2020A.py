from math import log
R = lambda : map(int,input().strip().split())
pn, pk, pa = 0,0,0
def log2(n,k):
    if k <= 1 or n < k:
        return n,0
    i = int(log(n,k))
    diff = n - k ** i
    return 1,diff

def Testcases(f=0):
    global pn, pk, pa
    n,k = R()
    if pn == n and pk == k:
        print(pa)
        return
    else:
        pn,pk = n,k
    x,diff = log2(n,k)

    while diff >= k:
        z = log2(diff,k)
        x,diff = x + z[0], z[1]

    pa = x + diff
    print(x + diff)

    pass
for T in range(int(input())):
    if T == -1:
        Testcases(f=1)
    else:
        Testcases()
