# Find smallest number in rotated sorted array

# O(log n)
import math

def rotated_array(arr):
    target = math.inf
    l, u = 0, len(arr)-1
    while l <= u:
        m = (l+u)//2
        # Identify the sorted half left or right
        if arr[m] <= arr[u]:
            target = min(target, arr[m])
            u = m-1
        else:
            target = min(target, arr[l])
            l = m+1
    return target

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    ans = rotated_array(arr)
    print(f"Smallest element in the array: {ans}")
