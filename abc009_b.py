N = int(input())
d_list = [int(input()) for i in range(N)]
x = sorted(set(d_list))

print(x[-2])
