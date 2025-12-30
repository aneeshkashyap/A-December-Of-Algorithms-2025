N = int(input())
arr = list(map(int, input().split()))

total_sum = N * (N + 1) // 2
total_sq_sum = N * (N + 1) * (2*N + 1) // 6

arr_sum = sum(arr)
arr_sq_sum = sum(x*x for x in arr)

diff = total_sum - arr_sum           # missing - duplicate
sq_diff = total_sq_sum - arr_sq_sum # missing^2 - duplicate^2

missing = (diff + sq_diff // diff) // 2
duplicate = missing - diff

print("Missing Number:", missing)
print("Duplicate Number:", duplicate)
