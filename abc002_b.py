W = list(input())
remove_list = ['a', 'i', 'u', 'e', 'o']


def remove_all(lst, x):
    for i in range(lst.count(x)):
            lst.remove(x)
    return lst


for i in remove_list:
    remove_all(W, i)

W = ''.join(W)
print(W)
