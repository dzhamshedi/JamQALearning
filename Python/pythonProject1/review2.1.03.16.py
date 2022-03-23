print("Hello world", "Hello", sep="*", end="\n")

print("-" * 12)
print(("|" + " " * 10 + "|"), ("|" + " " * 10 + "|"), ("|" + " " * 10 + "|"), sep="\n")
print("-" * 12)

#Input Все что вводится в input является стрингом

name = input()
print(f'Hello {name}')


people = int(input("value: "))
if (people % 2) == 0:
    print(people // 2)
else:
    print((people // 2) + (people % 2))
