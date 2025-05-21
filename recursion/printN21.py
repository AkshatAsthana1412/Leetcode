def printN21(n:int, i=1):
    if i>n:
        return
    printN21(n, i+1)
    print(i)

def print12N(n:int):
    if n == 0:
        return
    print12N(n-1)
    print(n)

if __name__ == '__main__':
    n = int(input("Enter number n: "))
    print("Printing N to 1 using linear recursion: ")
    printN21(n)
    print("Printing 1 to N using backtracking: ")
    print12N(n)