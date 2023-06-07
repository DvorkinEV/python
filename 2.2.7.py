a = input()
b = input()
c = input()
print(a)
print(b)
print(c)





y = 0
sets = []
while y != 3:
    p = input()
    sets.append(p)
    y += 1
for items in sets:
    print(items)






print(input(), input(), input(), sep = '\n')

a, b, c = input(), input(), input()
print(a, b, c, sep="\n")


print(*[input() for _ in range(3)], sep='\n')