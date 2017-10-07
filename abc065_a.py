# coding: utf-8
X, A, B = map(int, input().split())

if abs(B) <= abs(A):
    print('delicious')

elif abs(A) < abs(B) <= abs(A + X):
    print('safe')

elif abs(X + A) < abs(B):
    print('dangerous')
