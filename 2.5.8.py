n = int(input())
a = n//100
b = n//10%10
c = n%10
print(a,b,c,sep = "")
print(a,c,b,sep = "")
print(b,a,c,sep = "")
print(b,c,a,sep = "")
print(c,a,b,sep = "")
print(c,b,a,sep = "")


a,b,c = input()
print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')

n = list(input())

for x in range( len(n)):
	for y in range( len(n)):
		for z in range( len(n)):
			if x != y and x != z and z != y:
				print(n[x] + n[y] + n[z])

from itertools import permutations
for i in permutations(input(), 3):
    print(''.join(i))


import itertools
print(*[''.join(t) for t in itertools.permutations(input())], sep='\n')




[print(*n, sep='') for n in __import__('itertools').permutations(input())]


a,b,c = input()
for i in (a,b,c):
    for j in (a,b,c):
        for x in (a,b,c):
            if x!=j and i!=j and x!=i:
                print(i+j+x)


from itertools import permutations

for i in permutations(input()):
	print(''.join(i))


print((lambda s: f'{s[0]+s[1]+s[2]}\n{s[0]+s[2]+s[1]}\n{s[1]+s[0]+s[2]}\n{s[1]+s[2]+s[0]}\n{s[2]+s[0]+s[1]}\n{s[2]+s[1]+s[0]}')(list(input())))




i = list(input())
print(i[0], i[1], i[2], sep='')
print(i[0], i[2], i[1], sep='')
print(i[1], i[0], i[2], sep='')
print(i[1], i[2], i[0], sep='')
print(i[2], i[0], i[1], sep='')
print(i[2], i[1], i[0], sep='')


num = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
order_list = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

for order in order_list:
    for char in order:
        print(num[alphabet.index(char.lower())], end='')
    print()

from itertools import permutations as pm

inp = list(input())
for item in pm(inp):
    print(*item, sep='')

from itertools import permutations
for i in permutations(str(input())):
    print("".join(i))


import itertools
numb = input()
seta = itertools.permutations(numb)
for i in seta:
        print(i[0]+i[1]+i[2])



a = [str(i) for i in input()]
print(f"{a[0]}{a[1]}{a[2]}", f"{a[0]}{a[2]}{a[1]}",
      f"{a[1]}{a[0]}{a[2]}", f"{a[1]}{a[2]}{a[0]}",
      f"{a[2]}{a[0]}{a[1]}", f"{a[2]}{a[1]}{a[0]}", sep="\n")

[print(comb) for comb in ["".join(i) for i in list(__import__("itertools").permutations(input(),3))]]


[print(a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a, sep='\n') for a, b, c in [[str(i) for i in input()]]]


def swap(start, list):
    for i in range(len(list)):
        end = (list[:i] + list[i + 1:])
        if len(end) == 2:
            [print(_, sep="", end="") for _ in start + [list[i]] + [end[-2]] + [end[-1]]];
            print()
            [print(_, sep="", end="") for _ in start + [list[i]] + [end[-1]] + [end[-2]]];
            print()
        else:
            swap(start + [list[i]], end)


swap([], [int(i) for i in input()])


(lambda a, b, c: print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep="\n"))(*input())


(lambda x = input(): print(x, x[0]+x[2]+x[1], x[1]+x[0]+x[2], x[1]+x[2]+x[0], x[2]+x[0]+x[1], x[2]+x[1]+x[0], sep="\n"))()


[print(''.join(i)) for i in list(__import__('itertools').permutations(input()))]


