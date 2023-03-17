n = int(input())
if n != 0:
    dp = [0] * (n + 1)
    dp[1] = 0
    for n in range(2, n + 1):
        minimal = dp[n - 1] + 1
        if n % 2 == 0:
            minimal = min(minimal, dp[n // 2] + 1)
        if n % 3 == 0:
            minimal = min(minimal, dp[n // 3] + 1)
        dp[n] = minimal
    operations = []
    i = n
    while i > 1:
        if dp[i] == (dp[i - 1] + 1):
            operations.append(1)
            i -= 1
            continue
        if i % 2 == 0 and dp[i] == dp[i // 2] + 1:
            operations.append(2)
            i //= 2
            continue
        operations.append(3)
        i //= 3
    print(dp[n])
    num = 1
    print(num, end=' ')
    for i in range(len(operations)):
        op = operations.pop()
        if op == 3:
            num *= 3
        elif op == 2:
            num *= 2
        else:
            num += 1
        print(num, end=' ')
else:
    print(0)
    print(1, end='')
