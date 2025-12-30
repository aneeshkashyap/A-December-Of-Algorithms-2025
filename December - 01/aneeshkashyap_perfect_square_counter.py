n = int(input())
count = 0
i = 1

while i * i <= n:
    square = i * i
    print(square)
    count += 1
    i += 1

print(count)
