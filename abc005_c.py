T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


def judge(t, a, b):
    if N < M:
        print('no')
    else:
        for i in range(len(B)):
            if 0 <= B[i] - A[i] <= T:
                pass
            else:
                print('no')
                break
        else:
            print('yes')


judge(T, A, B)
