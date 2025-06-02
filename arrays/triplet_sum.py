# find all unique tiplets in arr whose sum is k
# Use two pointers approach for this, because we already know we need to find only 3 such elements
# backtracking will be inefficient here because we already know the number of elements we need to sum
# backtracking is used when you need to check all combinations/permutations of varying no. of elements
# O(n^2)
def triplet_sum(arr, k):
    s = 0
    n = len(arr)
    arr.sort()
    ans = set()
    for i in range(0, n-2):
        l, u = i+1, n-1
        while l < u:
            s = arr[i] + arr[l] + arr[u]
            if s == k:
                ans.add((arr[i], arr[l], arr[u]))
                l += 1
                u -= 1
            elif arr[i] + arr[l] + arr[u] > k:
                u -= 1
            else:
                l += 1
    return ans

if __name__ == '__main__':
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter sum required: "))
    res = triplet_sum(arr, k)
    for i, j, z in res:
        print(f'{i} + {j} + {z} = {k}')