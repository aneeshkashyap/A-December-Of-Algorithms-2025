from collections import deque

students = deque(map(int, input().split()))
sandwiches = list(map(int, input().split()))

while students and sandwiches:
    if students[0] == sandwiches[0]:
        students.popleft()      # student takes sandwich
        sandwiches.pop(0)       # remove sandwich from stack
    else:
        students.append(students.popleft())  # move student to end

print(len(students))
