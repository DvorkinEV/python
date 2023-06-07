a1 = int(input())
d = int(input())
n = int(input())
a = a1 + d*(n - 1)
print(a)


x = [int(input()) for _ in range(3)]
print(x[0] + x[1] * (x[2] - 1))


(lambda a, d, n: [print(a+d*(n-1))])(*(int(input()) for _ in range(3)))



print(int(input())+int(input())*(int(input())-1))



def progres(a, d, n):
    print(a + d * (n - 1))
progres(int(input()), int(input()), int(input()))



def f(a1, d, n):
    return a1 + d*(n - 1)

ans = []
for i in range(3):
    ans.append(int(input()))

print(f(ans[0], ans[1], ans[2]))




a1 = int(input())
d = int(input())
showN = int(input())
ariphmeticProggression = 0
count = 0

while count < 50:
  ariphmeticProggression = a1 + d
  count += 1
  if ariphmeticProggression == showN:
      break

n = a1 + (d*(showN - 1))

print(n)



a1,d,n = (int(input()) for i in range(3))
print(a1 + d * (n - 1))


def o():
  return int(input())
print(o()+o()*(o()-1))


def func(a,b,c):
    return a + b*(c - 1)
print(func(int(input()), int(input()), int(input())))


a, b, c = int(input()), int(input()), int(input())
print(f'{a + b * (c - 1)}')