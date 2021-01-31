s = 'C3H7'
total = 0
count = 0
for i in range(len(s)):
    if s[i].isalpha():
        continue
    total = count + int(s[i])
    count = count + 1

print(total)
print(count)