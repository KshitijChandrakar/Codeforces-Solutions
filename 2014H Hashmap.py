
def TestCases():
    n,q = [int(i) for i in input().split(" ") ]
    # scores = [int(i) for i in input().split(" ")]
    scoresStr = [int(i) for i in input().split(" ")]
    scoresMap = {}
    for i in range(n):
        if scoresStr[i] not in scoresMap:
            scoresMap[scoresStr[i]] = 1
        else:
            scoresMap[scoresStr[i]] += 1
    ##print(scoresMap)
    for i in range(q):
        l,r = [int(i) for i in input().split(" ")]
        currentTurn = 0
        scores = [0,0]
        scoresMap1 = scoresMap.copy()
        if l == r:
            #print("A")
            subScore = scoresStr[l-1]
        elif l == 1 and r == n:
            #print("C")
            subScore = []
        elif r == n:
            #print("B")
            subScore = scoresStr[:l-1]
        elif l == 1 and r != n:
            #print("D")
            subScore = scoresStr[r:]
        else:
            #print("E")
            subScore = scoresStr[:l] + scoresStr[r-1:]

        if str(type(subScore)) == "<class 'int'>":
            subScore = [subScore,]
        #print("Q =", i, "l,r =", l,r)
        #print(scoresMap, "|", subScore)
        for i in subScore:
            scoresMap[i] -= 1
        #print(scoresMap)

        for i in sorted(scoresMap.keys())[::-1]:
            if scoresMap[i]%2 == 0:
                scores[0] += scoresMap[i]/2 * i
                scores[1] += scoresMap[i]/2 * i
            else:
                scores[0] += (scoresMap[i]//2 + 1) * i
                scores[1] += scoresMap[i]//2 * i
        scoresMap = scoresMap1.copy()
        del scoresMap1

        print("YES" if scores[0] <= scores[1] else "NO")

T = int(input(""))
for t in range(T):
    ##print('======')
    TestCases()
