s = input()
s = s[::-1]

for i in s:
    if i == 'a':
        s = s.replace(i, '0')
    elif i == 'e':
        s = s.replace(i, '1')
    elif i == 'i':
        s = s.replace(i, '2')
    elif i == 'o':
        s = s.replace(i, '2')
    elif i == 'u':
        s = s.replace(i, '3')
print(s + "aca")
