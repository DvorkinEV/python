n = int(input())
k = int(input())
print(k//n)
print(k%n)



[print(f'{m//s}\n{m%s}') for s,m in [[int(input()) for _ in 'sm']]]


print(*(lambda x,y: (y//x,y%x))(int(input()),int(input())),sep='\n')


n, k = map(int, [input() for _ in range(2)]);print(k // n, k % n, sep = "\n")


[print(b // a, b % a, sep='\n') for a, b in [[int(input()) for _ in 'ab']][::-1]]


n, k = [int(input()) for i in range(2)]
print(k // n, k % n, sep='\n')



from sys import *

for n, k in ([int(i.strip()) for i in stdin.readlines()],):    stdout.write(f'{k // n}\n{k % n}')


a, b, = int(input()), int(input())
for i in range(1):
    print(b//a)
    print(b%a)



(lambda a, b: print(*divmod(b, a), sep='\n'))(int(input()), int(input()))

(lambda a, b: [print(f"{b//a}\n{b%a}")])(*(int(input()) for _ in range(2)))