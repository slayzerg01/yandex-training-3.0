with open('input.txt', 'r') as file:
    n = int(file.readline())
    k = int(file.readline())
    r = int(file.readline())
    p = int(file.readline())
    index = 2 * (r - 1) + (p - 1)
    pVar = (index + 1) % k
    i = k
    check1, check2 = True, True
    stop = False
    otv = []
    while check1 or check2:
        if index + i < n:
            if (index + i + 1) % k == pVar:
                otv.append(index + i)
                stop = True
        else:
            check1 = False
        if index - i >= 0:
            if (index - i + 1) % k == pVar:
                otv.append(index - i)
                stop = True
        else:
            check2 = False
        if stop:
            break
        i += k
if len(otv) == 0:
    print(-1)
elif len(otv) != 1:
    if (otv[0] // 2 + 1) - r <= r - (otv[1] // 2 + 1):
        otv = otv[0]
        print(otv // 2 + 1)
        print(otv % 2 + 1)
    else:
        otv = otv[1]
        print(otv // 2 + 1)
        print(otv % 2 + 1)
else:
    otv = max(otv)
    print(otv // 2 + 1)
    print(otv % 2 + 1)
