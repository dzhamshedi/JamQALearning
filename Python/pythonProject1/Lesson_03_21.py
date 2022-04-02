# def inc_fuction(x):
#     """Increase X by 1
#     """
#     x = x + 1
#     print(x)
#
# inc_fuction(5)

# def sum_function(x, y):
#     result = x + y
#     return result
#
# a1 = 14
# b1 = 23
# res = sum_function(a1, b1)
# print(f"res1ult: {res}")

# def compare_function(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
# print(compare_function(3, 4))

# def compare_function(x, y):
#     if x > y:
#         return x
#     else:
#         return 0
#
# print(compare_function(7, 5))

# x = 45
#
# def dummy_function():
#     x = 12
#     x += 1
#     print(x)
#
# dummy_function()
# print(x)

x = 45

def dummy_function():
    # global x если вписать глобальную переменную внутрь функции, глобальное значение перепишется
    x = 12
    x += 1
    print(x)

dummy_function()
print(x)

