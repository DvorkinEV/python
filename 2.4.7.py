a = int(input())
b = int(input())
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")


a,b = int(input()),int(input())
print(f'{a} + {b} = {a+b}', f'{a} - {b} = {a-b}', f'{a} * {b} = {a*b}', sep='\n')



a, b = int(input()), int(input())
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))