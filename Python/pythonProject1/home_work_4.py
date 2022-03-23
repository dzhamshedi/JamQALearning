for letter in "Hello Python!":
    print(letter)

i = 1
while i <= 100:
    print(i)
    if i == 45:
        break
    i += 1

for i in range(1, 21):
    if (i % 2) == 0:
        print(i)

for i in range(1, 31):
    if (i % 2) != 0:
        print(i)

abc = "abcdefghij"

for i in range(1, 11):
    print(i, abc[i-1])

for i in range(30, -1, -1):
    print(i)