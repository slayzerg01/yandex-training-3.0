with open("input.txt", "r") as file:
    n, m = map(int, file.readline().split())
    if n > 1 and m > 1:
        dp = []
        for i in range(n):
            dp.append([0] * m)
        for i in range(n):
            temp = list(map(int, file.readline().split()))
            for j in range(m):
                dp[i][j] = temp[j]
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    elif j > 0:
                        dp[i][j] += dp[i][j - 1]
        print(dp[n - 1][m - 1], end='')
    else:
        if n == 1:
            dp = list(map(int, file.readline().split()))
            for i in range(1, m):
                dp[i] += dp[i-1]
        elif m == 1:
            dp = [0] * n
            dp[0] = int(file.readline())
            print(dp)
            for i in range(1, n):
                dp[i] += dp[i-1] + int(file.readline())
        print(dp[max(n, m)-1], end='')

