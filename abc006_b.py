N = int(input())
a = {}
a[1] = 0
a[2] = 0
a[3] = 1


def tribonacci(x):
    if x >= 4:
        for i in range(4, x+1):
            a[i] = (a[i-1] + a[i-2] + a[i-3]) % 10007


tribonacci(N)
print(a[N])
