# find smallest index i such that arr[i] >= target
def lower_bound(arr, target):
    n = len(arr)
    ans = n
    l, u = 0, n-1
    while l <= u:
        m = l + (u-l)//2
        # keep track of every 'm' index where arr[m] >= target, due to the nature of binary search
        # when the loop ends, we'll naturally have the smallest index for which arr[m] >= target
        if target <= arr[m]:
            ans = m
            u = m-1
        else:
            l = m+1
    return ans

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    target = int(input("Enter the element for which to find lower bound: "))
    print(f"Element found at: {lower_bound(arr, target)}")