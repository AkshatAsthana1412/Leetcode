from collections import deque
# O(mod * n)
def dijkstra(arr, start, end, mod):
    if start == end:
        return 0
    q = deque([(0, start)])
    steps = [2*mod]*mod
    visited = [0]*mod
    while q:
        step, node = q.popleft()
        if node == end:
            return step
        if not visited[node]:
            visited[node] = 1
            for ele in arr:
                neighbor = (ele * node)%mod
                if not visited[neighbor]:
                    steps[neighbor] = step+1
                    q.append((step+1, neighbor))
    return -1


def minimum_multiplications(arr, start, end, mod):
    return dijkstra(arr, start, end, mod)

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    start, end, mod = int(input("Enter start number: ")), int(input("Enter end number: ")), int(input("Enter modulo number: "))
    print(minimum_multiplications(arr, start, end, mod))
