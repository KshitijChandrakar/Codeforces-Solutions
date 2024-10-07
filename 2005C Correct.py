for _ in range(int(input())):
    n, m = map(int, input().split())
    f = [-(10**9)] * 5
    f[0] = 0
    for _ in range(n):
        s = [c for c in ["narek".find(c) for c in input()] if c != -1] # Store indexes of every letter in input
        g = f.copy() # Make of a copy of f
        for i in range(5):
            x, y = i, f[i]
            for c in s:
                y -= 1
                if c == x:
                    x = (x + 1) % 5
                    if x == 0:
                        y += 10
            g[x] = max(g[x], y)
        f = g
    print(max(f))
