a = list(map(int, input().split()))
target = int(input())

start = 0
curr_sum = 0
found = False

for end in range(len(a)):
    curr_sum += a[end]

    while curr_sum > target and start <= end:
        curr_sum -= a[start]
        start += 1

    if curr_sum == target:
        print(start, end)
        found = True
        break

if not found:
    print(-1, -1)
