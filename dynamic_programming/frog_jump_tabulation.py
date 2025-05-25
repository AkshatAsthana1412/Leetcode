import math
# O(n) tabulation solution dp
def frog_jump(stairs):
    n = len(stairs)
    dp = [-1] * n
    dp[0] = 0
    ss = math.inf
    for i in range(1, n):
        fs = dp[i-1] + abs(stairs[i] - stairs[i-1])
        if i > 1:
            ss = dp[i-2] + abs(stairs[i] - stairs[i-2])
        dp[i] = min(fs, ss)
    return dp[n-1]

if __name__ == '__main__':
    st = list(map(int, input("Enter list elements: ").split()))
    n = len(st)
    print(frog_jump(st))