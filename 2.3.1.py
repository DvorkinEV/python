print("I", "like", "Python", sep='***')



print('I', end='***')
print('like', end='***')
print('Python')


print(*[chr(x) for x in [73, -10, 42, -5, 42,
                         -7, 42, 108, -78, 105,
                         107, 0, 101, 42, -3, 42,
                         -7, 42, 80, 121, -15, 116,
                         104, -3, 111, -12, -5, 110] if x > 0], sep='')



words = ['I', 'like', 'Python']
print(words[0], words[1], words[2], sep='***')


print(*'I like Python'.split(), sep='***')


values = ['I', 'like', 'Python']
print('***'.join(values))