a = int(input())
print(a)
print(a+1)
print(a+2)


print(*(lambda a: [a + i for i in range(3)])(int(input())),  sep='\n')


a = int(input())
print(a, a + 1, a + 2, sep="\n")


[print(i,i+1,i+2,sep='\n') for i in [int(input())]]


x = int(input())
[print(x + i) for i in range(3)]


print(a:=int(input()), a+1, a+2, sep='\n')


a = int(input())
b = a
while b <= a + 2:
    print(b)
    b = b + 1