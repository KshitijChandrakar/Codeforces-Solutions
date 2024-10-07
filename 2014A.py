R = lambda : map(int,input().strip().split())
def Testcases():
    n,k = R()
    a = list(R())
    gold = 0
    count = 0
    
    for i in range(n):
        if a[i] >= k:
            gold += a[i]
        elif gold>0 and a[i] == 0:
            count += 1
            gold -= 1
        pass
    print(count)
    pass
for _ in range(int(input())):
    Testcases()
