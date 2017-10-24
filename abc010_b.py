N = int(input())
N_list = map(int, input().split())


def arrange(x):
    cnt = 0
    for i in iter(x):
        if i % 6 == 0:
            cnt += 3
        elif i % 3 == 2:
            if (i - 1) % 2 == 0:
                cnt += 2
            else:
                cnt += 1
        elif i % 2 == 0:
            cnt += 1
    return cnt


print(arrange(N_list))
