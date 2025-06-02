import math
# O(n * log(max(arr)))
def div_sum(arr, num):
    s = 0
    for i in arr:
        s += math.ceil(i/num)
    return s

def smallest_divisor(arr, threshold):
    min_ele, max_ele = 1, max(arr)
    # linear search
    # for i in range(min_ele, max_ele+1):
    #     print(div_sum(arr, i))
    #     if div_sum(arr, i) <= threshold:
    #         return i
    # converting to binary search
    if threshold < len(arr):
        return -1
    l, u = min_ele, max_ele
    while l <= u:
        div = (l+u)//2
        ans = max_ele
        if div_sum(arr, div) <= threshold:
            u = div-1
            ans = min(ans, div)
        else:
            l = div+1
    return ans

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array elements: ").split()))
    threshold = int(input("Enter the threshold: "))
    ans = smallest_divisor(arr, threshold)
    print(f"smallest divisor: {ans}")

