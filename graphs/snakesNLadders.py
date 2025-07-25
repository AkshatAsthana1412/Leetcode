n = 4
for i in range(n):
    for j in range(n):
        if i & 1:
            print(f"{(i,j)}: {n*(n-i+1)-j}")
        else:
            print(f"{(i,j)}: {n*(n-i)+(j+1)}")