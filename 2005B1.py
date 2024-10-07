'''
Case 1:
m = 1
if q < m:
    return m # - q + q
if m < q:
    return n - m


Case 2:
    Get the difference betwee

'''

median = lambda a,b: ((b - a)/2) + (1 if (b - a)%2 == 0 else 0.5)

n,m,q,B,Q = 0,0,0,[],[]

def Cases(curQuery):
    global n,m,q,B,Q
    if m == 1:
        # print("Case 1")
        return B[0] if curQuery < B[0] else n - B[0]

    min1 = 0
    # # print(B)
    B.sort()
    for i in range(len(B)):

        min1 = i if abs(B[i] - curQuery) < abs(B[min1] - curQuery) else min1
    if (m-1 > min1 > 0) and (B[0] < curQuery < B[m-1])  and m > 1:
        if curQuery > B[min1]:
            # print("A")
            min2 = min1 + 1
        else:
            # print("B")
            min2 = min1 - 1
            min1, min2 = min2, min1
    elif not (m-1 > min1 > 0) and m > 1:
        if (B[0] < curQuery < B[m-1]):
            if curQuery > B[min1]:
                # print("C")
                min2 = min1 + 1
            else:
                # print("D")
                min2 = min1 - 1
                min1, min2 = min2, min1
        else:
            # print("E")
            min2 = min1
    else:
        # print("F")
        min2 = min1
    mid = median(B[min1], B[min2])
    # print("Min:",min1, min2, mid)


    if (not (m-1 > min1 > 0)) and (curQuery > B[m-1] or curQuery < B[0]): # Can Run to Edge
        # print("Case 2")
        return B[min1] - 1 if curQuery < B[min1] else n - B[min1]
    

    if min1 != min2: # Bound by the edges
        # print("Case 3")
        return min(abs(B[min1] - mid), abs(B[min2] - mid))
    else:
        # print("Case 4")
        return B[min1] if curQuery < B[min1] else n - B[min1]




def TestCases():
    global n,m,q,B,Q
    n, m, q = [int(i.strip()) for i in input().strip().split(" ")]
    B = [int(i.strip()) for i in input().strip().split(" ")]
    Q = [int(i.strip()) for i in input().strip().split(" ")]
    # # print(B, Q)
    for i in Q:
        print(int(Cases(i)))

    pass
for t in range(int(input())):
    # print("="* 10)
    TestCases()
