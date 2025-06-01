# finding element in a rotated sorted array with duplicates
# O(log n)
def bin_search(target, arr, l, u):
    while l <= u:
        m = (l+u)//2
        if arr[m] == target:
            return True
        if target < arr[m]:
            u = m-1
        else:
            l = m+1
    return False

def rotated_array(target, arr):
    l, u = 0, len(arr)-1
    ans = False
    while l <= u:
        m = (l+u)//2
        if arr[m] == target:
            return True
        # case when finding the sorted half is not possible, shrink the array in such case
        # arr[m] is anyways not the target
        if arr[m] == arr[u] and arr[m] == arr[l]:
            l += 1
            u -= 1
        # otherwise follow the same search process for rotated array
        elif arr[m] <= arr[u]:
            if arr[m] < target and target <= arr[u]:
                return bin_search(target, arr, m, u)
            else:
                u = m-1
        else:
            if arr[l] <= target and target < arr[m]:
                return bin_search(target, arr, l, m)
            else:
                l = m+1
    return ans

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    ele = int(input("Enter the element to be found: "))
    print(f"Element found: {rotated_array(ele, arr)}")