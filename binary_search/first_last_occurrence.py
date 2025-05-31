def lower_bound(target, arr):
    l,u = 0, len(arr)-1
    ans = len(arr)
    while l <= u:
        m = (l+u)//2
        if arr[m] >= target:
            ans = m
            u = m-1
        else:
            l = m+1
    return ans

def upper_bound(target, arr):
    l, u = 0, len(arr)-1
    ans = len(arr)
    while l <= u:
        m = (l+u)//2
        if arr[m] > target:
            ans = m
            u = m-1
        else:
            l = m+1
    return ans

def first_last_occurrence(target, arr):
    lb, ub = (lower_bound(target, arr), upper_bound(target, arr))
    if lb >= len(arr) or arr[lb] != target:
        return -1, -1
    else:
        return lb, ub-1
    
if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    target = int(input("Enter the element to be found: "))
    ans = first_last_occurrence(target, arr)
    print(f"First occurrence: {ans[0]}, last occurrence {ans[1]}")