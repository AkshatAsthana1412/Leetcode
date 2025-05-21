def subsequence_sum(alist, n, k, i=0, sum = 0, arr = []):
    if i >= n:
        if sum == k:
            print(arr)
            return True
        else:
            return False
    arr.append(alist[i])
    sum += alist[i]
    if subsequence_sum(alist, n, k, i+1, sum, arr):
        return True
    sum -= arr.pop()
    if subsequence_sum(alist, n, k, i+1, sum, arr):
        return True
    return False

if __name__ == '__main__':
    l = list(map(int, input("enter the array elements: ").split()))
    k = int(input("Enter the desired sum: "))
    subsequence_sum(l, len(l), k)