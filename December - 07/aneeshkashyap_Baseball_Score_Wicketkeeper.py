operations = input().split()  # e.g., 5 2 C D +

stack = []

for op in operations:
    if op == "C":
        stack.pop()
    elif op == "D":
        stack.append(2 * stack[-1])
    elif op == "+":
        stack.append(stack[-1] + stack[-2])
    else:
        stack.append(int(op))

print(sum(stack))
