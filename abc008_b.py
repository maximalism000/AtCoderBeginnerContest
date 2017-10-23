import collections
N = int(input())
alist = [input() for i in range(N)]

count_dict = collections.Counter(alist)

x = count_dict.most_common(1)

print(x[0][0])
