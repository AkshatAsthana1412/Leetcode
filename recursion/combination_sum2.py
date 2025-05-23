def combination_sum2(alist, n, k, ans=[], i=0, arr=[], sum=0):
    if sum == k:
        # remember to append arr.copy() instead of arr in ans, because ans.append(arr) means appending
        # a reference of arr to ans, which keeps on changing, so append the current state of arr in ans
        # to store the result, if you add ans.append(arr) the answer at the end of all recursions will be
        # [[]] because at the end of all recursion, arr becomes [], i.e. it's initial value
        ans.append(arr.copy())
        return
    
    if sum > k:
        return
    
    ele = None
    for j in range(i, n):
        if alist[j] == ele:
            continue
        arr.append(alist[j])
        sum += alist[j]
        combination_sum2(alist, n, k, ans, j+1, arr, sum)
        ele = arr.pop()
        sum -= ele
    return ans

if __name__ == '__main__':
    alist = list(map(int, input("Enter array elements: ").split()))
    n = len(alist)
    k = int(input("enter target sum: "))
    print(combination_sum2(sorted(alist), n, k))