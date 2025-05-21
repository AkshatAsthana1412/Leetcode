def reverse(alist, i=0):
    j = len(alist) - i - 1
    if i >= j:
        return alist
    alist[i], alist[j] = alist[j], alist[i]
    return reverse(alist, i+1)

if __name__ == '__main__':
    l = list(map(int, input("enter array elements: ").split()))
    print(reverse(l))