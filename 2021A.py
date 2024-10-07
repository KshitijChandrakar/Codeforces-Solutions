from bisect import bisect_left as bisect
def pop_two_elements(arr, index1, index2):
    # Ensure index2 is larger, so popping the first doesn't affect the position of the second
    if index1 > index2:
        index1, index2 = index2, index1

    elem1 = arr.pop(index1)
    elem2 = arr.pop(index2 - 1)  # Index2 has shifted after popping index1
    return elem1, elem2
def IdkSum(Arr):
    if len(Arr) <= 1:
        return Arr
    else:
        sum = 0
        l,m = 0,-1
        found = 0
        if Arr[-1] %2 == 0:
            for j in range(-2, -(1 + len(Arr)) , -1):
                if Arr[j] % 2 ==0:
                    sum = (Arr[-1] + Arr[j])//2
                    print(j, sum)
                    found = 1
                    l = j

                    break
        else:
            for j in range(-2, -(1 + len(Arr)) , -1):
                if Arr[j] % 2 ==1:
                    sum = (Arr[-1] + Arr[j])//2
                    print(j, sum)
                    found = 1
                    l = j
                    break
        if found:
            Arr.pop(-1)
            Arr.pop(l + 1)
            Arr.insert(bisect(Arr,sum),sum)
        else:
            sum = (Arr[-1] + Arr[-2])//2
            Arr.pop(-1)
            Arr.pop(-1)
            Arr.insert(bisect(Arr,sum),sum)
        print(Arr,l,m)
        return IdkSum(Arr)
def TestCases():
    n = int(input())
    Arr = [int(i) for i in input().strip().split()]
    Arr.sort()
    print(Arr)
    print(IdkSum(Arr), "A")

for _ in range(int(input())):
    TestCases()
