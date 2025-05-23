def fibonacci(n, res):
    if n < 2:
        return n
    if res[n] == -1:
        res[n] = fibonacci(n-1, res) + fibonacci(n-2, res)
    return res[n]

def fibonacci_bottom_up(n, res):
    res[0], res[1] = 0, 1
    for i in range(2, n+1):
        res[i] = res[i-1]+res[i-2]
    return res[n]

if __name__ == '__main__':
    n = int(input(("Enter number:")))
    res = [-1]*(n+1)
    print(fibonacci_bottom_up(n, res))
    