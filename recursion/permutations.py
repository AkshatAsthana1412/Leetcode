from collections import Counter
def permutations(arr, n, visited, res=[], ans=set()):
    if len(res) == n:
        ans.add(tuple(res.copy()))

    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        res.append(arr[i])
        permutations(arr, n, visited, res, ans)
        res.pop()
        visited[i] = 0
    return ans

if __name__ == '__main__':
    l = [1,2,3]
    d = [0]*len(l)
    print(permutations(l, 3))
