# COMPLEXITY 2^N
def subsequence_sum(alist, n, k, i=0, sum = 0, arr = []):
    if i >= n:
        if sum == k:
            print(arr)
        return
    arr.append(alist[i])
    sum += alist[i]
    subsequence_sum(alist, n, k, i+1, sum, arr)
    sum -= arr.pop()
    subsequence_sum(alist, n, k, i+1, sum, arr)

def print_one_subsequence(alist, n, k, arr=[], i=0, sum=0):
    if i >= n:
        if sum == k:
            print(arr)
            return True
        return False
    arr.append(alist[i])
    sum += alist[i]
    if print_one_subsequence(alist, n, k, arr, i+1, sum):
        return True
    sum -= arr.pop()
    if print_one_subsequence(alist, n, k, arr, i+1, sum):
        return True
    return False

    
def get_num_sequences_with_sum(alist, n, k, i=0, sum=0):
    if i >= n:
        if sum == k:
            return 1
        else:
            return 0
    sum += alist[i]
    l = get_num_sequences_with_sum(alist, n, k, i+1, sum)
    sum -= alist[i]
    r = get_num_sequences_with_sum(alist, n, k,
                                    i+1, sum)
    return l + r

if __name__ == '__main__':
    l = list(map(int, input("enter the array elements: ").split()))
    k = int(input("Enter the desired sum: "))
    subsequence_sum(l, len(l), k)
    print("Printing any one subsequence matching this condition: ")
    print_one_subsequence(l, len(l), k)
    print(f"no. of subsequences with given sum: {get_num_sequences_with_sum(l, len(l), k)}")
