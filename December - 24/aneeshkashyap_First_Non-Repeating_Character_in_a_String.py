s = input()
for c in s:
    if s.count(c) == 1:
        print("The first non-repeating character is:", c)
        break
else:
    print("No non-repeating character found.")
