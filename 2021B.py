

from collections import defaultdict
def Mex(Arr):
    x = set(Arr)
    i = 0
    n = max(x)

    z = []
    while True:
        if i > n:
            break
        if i in x:
            i += 1
        else:
            z.append(x[i])
            i += 1
    return z
X = lambda i : (i//2, i%2)
def TestCases():
    n,x = [int(i) for i in input().strip().split()]
    Arr = [int(i) for i in input().strip().split()]
    CurMex = Mex(Arr)
    dupeA,dupeB,CurMexA,CurMexB = defaultdict(int),defaultdict(int),defaultdict(int),defaultdict(int)
    Arr.sort()
    Max = Arr[-1]
    for i in range(len(Arr)):
        if Arr[i] == Arr[i-1]:
            dupe.append(i)
    for i in range(len(CurMex)):
        a,b = X(CurMex[i])
        CurMexA[a] += 1
        CurMexB[b] += 1
    for i in range(len(dupe)):
        a,b = X(dupe[i])
        dupeA[a] += 1
        dupeB[b] += 1
        #dupeA[dupe[i]//x] = dupe[i]]%x
    for i in dupeB:
        if i in CurMexB:
            dupeB[i] = dupeB[i] - CurMexB[i]
            CurMexB[i] = -1 * (dupeB[i] - CurMexB[i])
            if dupeB[i] <= 0:
                del dupeB[i]
            else:
                del CurMexB[i]
    if len(list(CurMexB.keys())) > 0:

    # for i in range(len(dupe)):
    #     for j in range(len(CurMex)):



        '''
        if Arr[i] > CurMex:
            print(CurMex)
            return
        else:
            div, rem = Arr[i]//x, Arr[i]%x
            CurMexD, CurMexR = CurMex//x, CurMex%x
            if CurMexR == rem:
                Arr[i] = CurMex
                Arr2[CurMex] = 0
                CurMex = Mex(Arr2)
            else:
    ;'''

# for _ in range(int(input())):
#     TestCases()
