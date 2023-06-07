n = int(input())
print((n + 3)//4)


matrix = [[j for j in range(i-3, i+1)] for i in range(4, 38, 4)]
place = int(input())
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == place:
            print(*[i+1])



a = int(input())
one = [1, 2, 3, 4]
two = [5, 6, 7, 8]
three = [9, 10, 11, 12]
four = [13, 14, 15, 16]
five = [17, 18, 19, 20]
six = [21, 22, 23, 24]
seven = [25, 26, 27, 28]
eight = [29, 30, 31, 32]
nine = [33, 34, 35, 36]
if a in one:
    print(1)
else:
    if a in two:
        print(2)
if a in three:
    print(3)
else:
    if a in four:
        print(4)
if a in five:
    print(5)
else:
    if a in six:
        print(6)
if a in seven:
    print(7)
else:
    if a in eight:
        print(8)
if a in nine:
    print(9)

a = int(input())
for q in range(1, 5):
    q2 = 1
    if a == q:
        print(q2)
for w in range(5, 9):
    w2 = 2
    if a == w:
        print(w2)
for e in range(9, 13):
    e2 = 3
    if a == e:
        print(e2)
for r in range(13, 17):
    r2 = 4
    if a == r:
        print(r2)
for t in range(17, 21):
    t2 = 5
    if a == t:
        print(t2)
for y in range(21, 25):
    y2 = 6
    if a == y:
        print(y2)
for u in range(25, 29):
    u2 = 7
    if a == u:
        print(u2)
for i in range(29, 33):
    i2 = 8
    if a == i:
        print(i2)
for o in range(33, 37):
    o2 = 9
    if a == o:
        print(o2)



compartment_seat = int(input())
coupes = {1: [1, 2, 3, 4], 2: [5, 6, 7, 8], 3: [9, 10, 11, 12],
          4: [13, 14, 15, 16], 5: [17, 18, 19, 20], 6: [21, 22, 23, 24],
          7: [25, 26, 27, 28], 8: [29, 30, 31, 32], 9: [33, 34, 35, 36]}

for key, item in coupes.items():
    if compartment_seat in item:
        print(key)
        break


a = int(input())
r = 0

for i in range(0, 36, 4):
    if(a <= i): break;
    r = r+1
print(r)




c = int(input())
list_kupe = []
start = 1
fin = 4
for i in range(1,10):
    kupe = list(range(start,fin+1))
    list_kupe.append(kupe)
    start = start+4
    fin = fin+4

for index , item  in enumerate(list_kupe):
    if c in item:
        print(index+1)


def finding_a_place(x): # найти место
    railway_carriage = {1: [1, 2, 3, 4], 2: [5, 6, 7, 8], 3: [9, 10, 11, 12],
                        4: [13, 14, 15, 16], 5: [17, 18, 19, 20], 6: [21, 22, 23, 24],
                        7: [25, 26, 27, 28], 8: [29, 30, 31, 32], 9: [33, 34, 35, 36]}
    i = 1

    for place in railway_carriage:
        new_list = []
        # print(railway_carriage[place])
        for i in range(0, 4):
            new_list.append(railway_carriage[place][i])
        # print('...', new_list, '...')
        for p in new_list:
            # print(p)
            if p == x:
                # print('-------------',place)
                return place

n = int(input())
print(finding_a_place(n))


import math
a = int(input())
print(math.ceil(a / 4))


a = {1, 2, 3, 4}
b = {5, 6, 7, 8}
c = {9, 10, 11, 12}
d = {13, 14, 15, 16}
e = {17, 18, 19, 20}
f = {21, 22, 23, 24}
g = {25, 26, 27, 28}
h = {29, 30, 31, 32}
i = {33, 34, 35, 36}
n = int(input())
if n in a:
    print(1)
elif n in b:
    print(2)
elif n in c:
    print(3)
elif n in d:
    print(4)
elif n in e:
    print(5)
elif n in f:
    print(6)
elif n in g:
    print(7)
elif n in h:
    print(8)
elif n in i:
    print(9)


a = int(input())
b = 4
if a <= b:
    print(int(b / 4))
else:
    while True:
        if a > b:
            b += 4
        else:
            a <= b
            print(int(b / 4))
            break