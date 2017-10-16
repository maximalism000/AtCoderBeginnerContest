x = list('abcdefghijklmnopqrstuvwxyz')
dic = {}
count = 0
A = input()

for i in iter(x):
    dic[i] = count
    count += 1


if A == 'a':
    print(-1)
elif len(A) == 1:
    print('a')
else:
    print('a' * (len(A) - 1))
