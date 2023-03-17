def BinarySearch(lys, val):
    first = 0
    last = len(lys) - 2
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[-1] < val:
            index = len(lys)
        elif lys[-2] < val:
            index = len(lys) - 1
        elif lys[mid] == val:
            index = mid
        elif lys[mid] < val < lys[mid+1]:
            index = mid + 1
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if index == -1:
        if len(lys) == 1 and lys[0] < val:
            return 1
        else:
            return 0
    return index


with open('input.txt', 'r') as file:
    n = int(file.readline())
    nn = sorted(list(map(int, set(file.readline().split()))))
    k = int(file.readline())
    kk = list(map(int, file.readline().split()))
    
if n > 1000:
    for i in range(k):
        print(f"{BinarySearch(nn, kk[i])}")
else:
    for i in range(k):
        print(sum(j < kk[i] for j in nn))


