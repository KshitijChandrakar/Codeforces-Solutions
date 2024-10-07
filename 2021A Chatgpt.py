import heapq

def TestCases(arr):
    arr = [-x for x in arr]
    heapq.heapify(arr)
    while len(arr) > 1:
        a = -heapq.heappop(arr)
        b = -heapq.heappop(arr)
        new_element = (a + b) // 2
        
        heapq.heappush(arr, -new_element)
    return -arr[0]

for _ in range(int(input())):
    _ = input()
    print(TestCases([int(i) for i in input().strip().split()]))
