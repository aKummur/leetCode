from time import time

def fibDp(n, dp):
    if n<=1:
        dp[n] = n
        return dp[n]
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibDp(n-1, dp) + fibDp(n-2, dp)
    return dp[n]

def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

dp = [-1 for i in range(39)]
startTime = time()
print(fibDp(38, dp))
print("{0} secs".format(time() - startTime))

startTime = time()
print(fib(38))
print("{0} secs".format(time() - startTime))

def climbStairs(n):
    if n <= 2:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# practice 1
def climbStairs(n):
    if n <= 2:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]