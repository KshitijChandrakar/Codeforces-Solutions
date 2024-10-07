def sum2(n,k):
    if n < k:
        return 0
    else:
        return n ** n + sum2(n-1,k)
def sum3(n,k):
    return sum2(n, n+1-k)
print("n","k","sum")
for k in range(1,31):
    for n in range(1,30):
        if k<=n:
            if k % 4 == 3 and n%2 == 0:
                print("YES" if sum3(n,k)%2 == 0 else "NO", n,k)
