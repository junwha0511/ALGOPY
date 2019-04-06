n = int(input())

dp = [0 for i in range(n+2)]
dp[1] = 1
dp[2] = 2

def sum(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    if dp[n-1]==0:
        dp[n-1] = sum(n-1)
    if dp[n-2]==0:
        dp[n-2] = sum(n-2)
    dp[n] = dp[n-1]+dp[n-2]
    return dp[n]
print(sum(n)%10007)