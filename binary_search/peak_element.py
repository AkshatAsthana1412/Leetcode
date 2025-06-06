# O(log n)
# assuming there will always be a peak element
def peak_element(arr):
    n = len(arr)
    if len(arr) == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n-1] > arr[n-2]:
        return arr[n-1]
    l, u = 1, n-2
    while l <= u:
        m = (l+u)//2
        # check if this element is a peak
        if arr[m-1] < arr[m] and arr[m] > arr[m+1]:
            return arr[m]
        # check if we're on the increasing curve, if so, peak is furthur on the right
        elif arr[m] < arr[m+1] and arr[m-1] < arr[m]:
            l = m+1
        # if not, peak might be on the left half of the curve
        else:
            u = m-1

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    num = peak_element(arr)
    print(f"Peak element: {num}")
