# find smallest index i such that arr[i] > target
def upper_bound(arr, target):
    l, u = 0, len(arr)-1
    ans = (l+u)//2
    while l <= u:
        m = (l+u)//2
        if target < arr[m]:
            ans = m
            u = m-1
        else:
            l = m+1
    return ans

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    target = int(input("Enter the element for which to find lower bound: "))
    print(f"Element found at: {upper_bound(arr, target)}")