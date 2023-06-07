a = int(input())
b = int(input())
c = int(input())
print(a+b+c)


print(int(input()) + int(input()) + int(input()))


print(sum(int(input()) for _ in range(3)))

sum = 0
for i in range(3):
    num = int(input())
    sum+=num
print(sum)
