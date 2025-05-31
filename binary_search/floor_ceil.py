# floor is the largest no. in array <= target and ceil is smallest no. in array >= target
def floor_ceil(target:int, arr:list):
    l, u = 0, len(arr)-1
    ceil_ind = l
    while l <= u:
        m = (l+u)//2
        if target <= arr[m]:
            ceil_ind = m
            u = m-1
        else:
            l = m+1
    
    l, u = 0, len(arr)-1
    floor_ind = -1
    while l <= u:
        m = (l+u)//2
        if target>=arr[m]:
            l = m+1
            floor_ind = m
        else:
            u = m-1

    if arr[ceil_ind] < target:
        ceil_val = -1
    else:
        ceil_val = arr[ceil_ind]
    if arr[floor_ind] > target:
        floor_val = -1
    else:
        floor_val = arr[floor_ind]

    return floor_val, ceil_val

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    target = int(input("Enter the no. for which to find floor and ceil for: "))
    ans = floor_ceil(target, arr)
    print(f"Ceil: {ans[1]}, floor: {ans[0]}")