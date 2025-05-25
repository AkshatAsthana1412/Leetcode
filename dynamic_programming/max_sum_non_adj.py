# O(2^n) for pure recursive solution
# O(n) time for memoization and tabulation approach
# you should check if there are any overlapping subproblems before attempting memoization
def max_sum_of_non_adjacent(arr, indx, dp):
    if not arr:
        return None
    if indx == 0:
        # if recursion reaches here, that means I picked 2 in the last recursion call
        return arr[indx]
    if indx < 0:
        # possible when I picked 1 in the last call instead of 2. So I can only pick 1 - 2 = -1 indx, which is not possible
        return 0
    if dp[indx] != -1:
        return dp[indx]
    max_sum_with_pick = arr[indx] + max_sum_of_non_adjacent(arr, indx - 2, dp)
    max_sum_without_pick = max_sum_of_non_adjacent(arr, indx - 1, dp)
    dp[indx] = max(max_sum_with_pick, max_sum_without_pick)
    return dp[indx]

def max_sum_of_non_adjacent_tabulised(arr):
    n = len(arr)
    dp = [-1]*n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n):
        dp[i] = max(dp[i-2] + arr[i], dp[i-1])
    return dp[n-1]

if __name__ == '__main__':
    arr = list(map(int, input("Enter list elements: ").split()))
    n = len(arr)
    dp = [-1]*n
    # print(max_sum_of_non_adjacent(arr, n-1, dp))
    print(max_sum_of_non_adjacent_tabulised(arr))