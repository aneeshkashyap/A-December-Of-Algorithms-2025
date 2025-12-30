n = int(input())

if n % 2 == 0:
    print("Magic square is only possible for odd values of n.")
else:
    magic = [[0]*n for _ in range(n)]

    num = 1
    i, j = 0, n // 2   

    while num <= n*n:
        magic[i][j] = num
        num += 1

        ni = (i - 1) % n   
        nj = (j + 1) % n   

        if magic[ni][nj] != 0:   
            i = (i + 1) % n
        else:
            i, j = ni, nj
            
    for row in magic:
        print(*row)
