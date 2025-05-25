def subsets(alist, n, arr=[], indx=0, ans=[]):
    # NOTE very important, no condition to append arr here because, every recursion call
    # will generate a unique subset
    ans.append(arr.copy())
    ele = None
    for i in range(indx, n):
        if ele == alist[i]:
            continue
        arr.append(alist[i])
        subsets(alist, n, arr, i+1, ans)
        ele = arr.pop()
    return ans

if __name__ == '__main__':
    alist = list(map(int, input("Enter list elements: ").split()))
    n = len(alist)
    # NOTE remember to pass in the sorted array here to skip duplicates
    print(subsets(sorted(alist), n, [], 0, []))