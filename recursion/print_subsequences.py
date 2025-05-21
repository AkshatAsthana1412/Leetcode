def print_subsequences(alist, n, i=0, arr=[]):
    if i >= n:
        print(arr)
        return
    arr.append(alist[i])
    print_subsequences(alist, n, i+1, arr)
    arr.pop()
    print_subsequences(alist, n, i+1, arr)

if __name__ == '__main__':
    l = list(map(int, input("enter the array elements: ").split()))
    print_subsequences(l, len(l))