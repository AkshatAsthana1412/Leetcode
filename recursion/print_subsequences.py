def print_subsequences(alist, n, i=0, arr=[]):
    if i >= n:
        print(arr)
        return
    arr.append(alist[i])
    print_subsequences(alist, n, i+1, arr)
    arr.pop()
    print_subsequences(alist, n, i+1, arr)

def print_unique_subsequences(alist, n, i=0, arr=[], seen=set()):
    if i >= n:
        if tuple(arr) not in seen:
            print(arr)
            seen.add(tuple(arr))
        return
    arr.append(alist[i])
    print_unique_subsequences(alist, n, i+1, arr, seen)
    arr.pop()
    print_unique_subsequences(alist, n, i+1, arr, seen)

# def print_unique_subsequences(alist, n, i=0, arr=[]):
#     if i >= n:
#         print(arr)
#         return
#     if alist[i] in arr:
#         return
#     arr.append(alist[i])
#     print_unique_subsequences(alist, n, i+1, arr)
#     arr.pop()
#     print_unique_subsequences(alist, n, i+1, arr)

if __name__ == '__main__':
    l = list(map(int, input("enter the array elements: ").split()))
    print("printing all subsequences:")
    # print_subsequences(l, len(l))
    print("printing unique subsequences:")
    print_unique_subsequences(l, len(l))