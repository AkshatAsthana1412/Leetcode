import math
# this is the top-down approach with memoization
# O(n)
def frog_jump(stairs, i, dp):
    if i == 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    left = frog_jump(stairs, i-1, dp) + abs(stairs[i] - stairs[i-1])
    if i > 1:
        right = frog_jump(stairs, i-2, dp) + abs(stairs[i] - stairs[i-2])
    else:
        right = math.inf
    dp[i] = min(left, right)
    return dp[i]

if __name__ == '__main__':
    st = list(map(int, input("Enter list elements: ").split()))
    n = len(st)
    print(frog_jump(st, n-1, dp=[-1]*n))