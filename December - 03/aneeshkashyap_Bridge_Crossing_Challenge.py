stones = list(map(int, input().split()))

reach = 0

for i in range(len(stones)):
    if i > reach:
        print("false")
        break
    reach = max(reach, i + stones[i])

print("true" if reach >= len(stones) - 1 else "false")
