def max_sum_subarray(arr):
    if not arr:
        return 0, []
    l, r = 0, 0
    s = 0
    max_s = 0
    ind = [0,0]
    while r < len(arr):
        s += arr[r]
        if s > max_s:
            max_s = s
            ind = [l, r]
        r += 1
        # there is no benefit of keeping s -ve because it will only result in a smaller sum
        # for the subarray in the next step, e.g. if the next element is +ve, current element will reduce the 
        # total sum in the next step, than if we had only considered the subarray with the next element.
        # If the next element is -ve, it will definitely result in a larger -ve
        if s < 0:
            s = 0
            l = r

    return max_s, ind

print(max_sum_subarray([-2,-3,4,-1,-2,1,5,-3]))
        