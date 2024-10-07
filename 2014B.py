R = lambda : map(int,input().strip().split())
Mat = { # the keys are k%4
    # the list is n%2 as index
    0: [1,1],
    1: [1,0],
    2: [0,0],
    3: [0,1]
}
def Testcases():
    n,k = R()

    if k == 1:
        verdict = "NO" if n%2==1 else "YES"
    else:
        verdict = "NO" if Mat[k%4][n%2] == 0 else "YES"
    print(verdict)

for _ in range(int(input())):
    Testcases()
