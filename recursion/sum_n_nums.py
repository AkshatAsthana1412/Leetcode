def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

def fact(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    return n*fact(n-1)

if __name__ == '__main__':
    n = int(input("Enter number n: "))  
    print(sum(n))
    print(fact(n))