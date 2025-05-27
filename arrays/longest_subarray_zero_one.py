# problem is max consecutive ones 3
# after some thought it can be rephrased as longest subarray with at most k 0s
# hence it can be solved by sliding window
def longest_subarray(arr:list, k:int):
    zeros = 0
    max_len = 0
    l, r = 0, 0
    n = len(arr)
    while r < n:
        if arr[r] == 1:
            max_len = max(max_len, r - l + 1)
        elif arr[r] == 0:
            zeros += 1
            if zeros <= k:
                max_len = max(max_len, r-l+1)
            while zeros > k:
                if arr[l] == 0:
                    zeros -= 1
                l += 1
        r += 1
    return max_len

if __name__ == '__main__':
    arr = list(map(int, input("Enter array elememts: ").split()))
    k = int(input("Enter the no. of 0s permissible: "))
    print(longest_subarray(arr, k))
        

