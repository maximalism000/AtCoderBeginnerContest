N = int(input())


def caluculate_salary(x):
    sigma = 0
    for i in range(1, x+1):
        sigma += i * 10000
    return int(sigma / x)


print(caluculate_salary(N))
