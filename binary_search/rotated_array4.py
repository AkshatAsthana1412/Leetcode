# O(n)
# number of times array is rotated
# we just need to find the smallest number in the rotated array, and return it's index
import math
def rotated_array(arr):
    l, u = 0, len(arr) - 1
    ind = 0
    num = math.inf
    while l <= u:
        m = (l+u)//2
        if arr[m] <= arr[u]:
            if arr[m] <= num:
                num = arr[m]
                ind = m
            u = m-1
        else:
            if arr[l] <= num:
                num = arr[l]
                ind = l
            l = m+1
    return ind, num

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    ind, num = rotated_array(arr)
    print(f"Number of times array needs to be rotated: {ind}")

