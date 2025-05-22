def combination_sum(alist, n, k, i=0, arr = [], sum=0):
    if i >= n:
        if sum == k:
            print(arr)
            return 1
        else:
            return 0
    if sum == k:
        print(arr)
        return 1
    if sum > k:
        return 0
    arr.append(alist[i])
    sum += alist[i]
    l = combination_sum(alist, n, k, i, arr, sum)
    sum -= arr.pop()
    r = combination_sum(alist, n, k, i+1, arr, sum)
    return l+r

if __name__ == "__main__":
    l = list(map(int, input("enter array elements: ").split()))
    n = len(l)
    k = int(input("Enter desired sum: "))
    # print(combination_sum([3,2,5,1], 4, 8))
    print(combination_sum(l, n, k))
        