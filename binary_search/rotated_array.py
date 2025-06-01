# O(log n)
def bin_search(arr, l, u, target):
    while l <= u:
        m = (l+u)//2
        if arr[m] == target:
            return m
        if target < arr[m]:
            u = m-1
        else:
            l = m+1
    return -1

def rotated_array(target, arr):
    l, u = 0, len(arr)-1
    while l <= u:
        m = (l+u)//2
        if arr[m] == target:
            return m
        # Identify the sorted half left or right
        if arr[m] <= arr[u]:
            # check if target lies in this half, if it is sorted
            if arr[m] < target and target <= arr[u]:
                # do a binary search on this half
                return bin_search(arr, m, u, target)
            else:
                u = m-1
        else:
            if arr[m] > target and target >= arr[l]:
                return bin_search(arr, l, m, target)
            else:
                l = m+1
    return -1

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    target = int(input("Enter the element to be found: "))
    ans = rotated_array(target, arr)
    print(f"Element found at: {ans}")
