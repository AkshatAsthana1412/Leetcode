def binary_search(ele, arr):
    l, u = 0, len(arr)-1
    m = (l+u)//2
    while l <= u:
        m = (l+u)//2
        if arr[m] == ele:
            return m
        if ele < arr[m]:
            u = m-1
        else:
            l = m+1
    return -1

def binary_search_recursive(ele, arr, l, u):
    if l > u:
        return -1
    m = (l+u)//2
    if arr[m] == ele:
        return m
    if ele < arr[m]:
        return binary_search_recursive(ele, arr, l, m-1)
    return binary_search_recursive(ele, arr, m+1, u)

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    ele = int(input("Enter the element to be found: "))
    print(f"Element found at: {binary_search_recursive(ele, arr, 0, len(arr)-1)}")