n, k = map(int, input().split())
dp = [0] * (n + 1)
if n == 1 or k == 1:
    print(1)
else:
    for i in range(k):
        if i <= n:
            dp[i] = 1
    for i in range(2, n + 1):
        dp[i] = sum(dp[max(i-k, 0):i])
    print(dp[n-1])