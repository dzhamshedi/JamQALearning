a = 14
b = 10
print(a > b)

a = 2
b = 3
print(a > b)

a1 = 8
b1 = 7

if a1 > b1:
    print(f"{a1} grater than {b1}")


a2 = 7
b2 = 8
if a2 < b2:
    print(f"{a2} is less than {b2}")

x3 = 10
y3 = -8  # -1, -2, -3, etc.

if (x3 > 0) and (y3 > 0):
    if x3 > y3:
        print(f'{x3} is greater than {y3}')
    else:
        print(f'{x3} is less than {y3}')
else:
    print("One or both numbers are not positive, "
          "can't proceed with the comparison!")

p = 12
o = 0

if p > 0 and o > 0:
    if o > p:
        print(f"{o} grater than {p}")
    else:
        print(f"{p}is less than {o}")
else:
    print("Value is < 0")
