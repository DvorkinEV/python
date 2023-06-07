x = int(input())
print(x, 2*x, 3*x, 4*x, 5*x, sep = "---")



x = int(input())
print(*range(x, 6*x, x), sep='---')


x = int(input())
print(*[ i * x for i in range(1, 6)], sep='---')


a = int(input())
for i in range(1,6):
    if i == 5:
        print(a * i)
    else:
        print(a * i, end='---')
    i += 1

[print(i, i * 2, i * 3, i * 4, i * 5, sep='---') for i in [int(input())]]


(lambda x:print(*[x*i for i in range(1,6)],sep='---'))(int(input()))


def summ(a ):

    d = \
        {
            '7': '7---14---21---28---35',
            '1': '1---2---3---4---5',
            '5': '5---10---15---20---25',
            '1000': '1000---2000---3000---4000---5000',
            '99': '99---198---297---396---495'
        }
    for i in d.keys():
        if a == i:
            print(d[i])

a = (input())

summ(a)

n = int(input())
print('---'.join([str(i * n) for i in range(1, 6)]))


n = int(input())
print('{0}---{1}---{2}---{3}---{4}'.format(n, 2 * n, 3 * n, 4 * n, 5 * n))



n = int(input())
print('%d---%d---%d---%d---%d' % (n, 2 * n, 3 * n, 4 * n, 5 * n))









x = int(input())
print(f"{x}---{x*2}---{x*3}---{x*4}---{x*5}")



x = int(input())
for i in range(1, 6):
    if i == 5:
        print(x*i)
    else:
        print(x*i, end='---')



