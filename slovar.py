a = ['hello', 'world', 'python']
print(a, 'количество слов=', len(a))
print('введите список с таким же количеством слов')
b = []
for i in range(len(a)):
    b.append(input())
print(b)
c = {}
for i in range(len(a)):
    c[a[i]] = b[i]
print(c)
