a = input()
b = input()
c = input()
print(c)
print(b)
print(a)



[print(i) for i in [input() for _ in range(3)][::-1]]


print(*reversed([input(), input(), input()]), sep="\n")


print("{2}\n{1}\n{0}\n".format(input(), input(), input()))