# this is the same logic as used in max_sum_non_adj.py
def f(arr):
    n = len(arr)
    dp = [-1]*n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n):
        dp[i] = max(arr[i] + dp[i-2], dp[i-1])
    return dp[n-1]

def house_robber(houses):
    # we cannot pick first and last house together, so we first calculate max/optimal sum for houses from first to last-1
    # this sum will be the optimal sum if we decide not to pick the last house since it assumes we may have picked the first house.
    # similarly, in another function call we can omit the first house and find optimal sum for the remaining array which assumes
    # we may have picked the last house if it is in the optimal solution, but then we don't have to pick the first house which we will
    # not, based on the array picked houses[1:].
    if len(houses) == 1:
        return houses[0]
    return max(f(houses[1:]), f(houses[:-1]))

if __name__ == '__main__':
    arr = list(map(int, input("Enter list elements: ").split()))
    n = len(arr)
    print(house_robber(arr))