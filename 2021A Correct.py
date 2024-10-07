# for s in[*open(0)][2::2]:
s = input()
a=sorted(map(int,s.split()))
while len(a)>1:
    a=a[2:]+[(a[0]+a[1])//2]
    a.sort()
print(*a)
