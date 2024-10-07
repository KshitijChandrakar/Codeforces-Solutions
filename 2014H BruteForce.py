def TestCases():
    n,q = [int(i) for i in input().split(" ") ]
    # scores = [int(i) for i in input().split(" ")]
    scoresStr = input().split(" ")
    for i in range(n):
        scoresStr[i] = [int(scoresStr[i]),i]
    scoresStr.sort(key=lambda x: x[0])
    for i in range(q):
        #print('-'*4)
        scores = [0,0]
        currentTurn = 0
        l,r = [int(i) for i in input().split(" ")]
        for i in range(-1,-n-1, -1):
            if l-1 <= scoresStr[i][1] <= r-1:
                #print(scoresStr[i], end = " ")
                scores[currentTurn] += scoresStr[i][0]
                currentTurn = not currentTurn
        #print()
        #print(scores)
        print("YES" if scores[0] <= scores[1] else "NO")

T = int(input(""))
for t in range(T):
    #print('======')
    TestCases()
