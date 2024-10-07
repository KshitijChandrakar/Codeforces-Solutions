from bisect import*
R=lambda:map(int,input().split())
t,=R()
while t:
    t-=1
    n,*_=R()
    b=sorted(R())
    # print(b)
    b=1-b[0],*b,2*n-b[-1]
    # print(b)
    for x in R():i=bisect(b,x);print(b,max(1,b[i]-b[i-1]>>1))
'''
3
10 2 1
1 4 8 12
2
8 2 1
3 6
1
8 2 1
3 6 7
8
'''
