n = int(input())
dp = [0] * (n + 2)
dp[0], dp[1] = 1, 1
dp[2] = 2
for i in range(3, n + 2):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
print(dp[n+1])