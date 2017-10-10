S = input()
T = input()
at_mark_lst = list('atcoder')

bool_list = []
false_index = []
at_mark_bool = []


def get_bool_list(lst1, lst2):
    for i in range(len(lst1)):
        boolean = lst1[i] == lst2[i]
        bool_list.append(boolean)
    return bool_list


def get_false_index(boo_lst):
    for i in range(len(boo_lst)):
        if not boo_lst[i]:
            false_index.append(i)
    return false_index


def win_or_lose(boo_lst, fal_in, lst1, lst2):
    # All True
    if False not in boo_lst:
        print('You can win')
    elif ('@' in lst1) or ('@' in lst2):
        for i in fal_in:
            if lst1[i] == '@' and lst2[i] in at_mark_lst:
                at_mark_bool.append(True)
            elif lst2[i] == '@' and lst1[i] in at_mark_lst:
                at_mark_bool.append(True)
            else:
                at_mark_bool.append(False)
        if False not in at_mark_bool:
            print('You can win')
        else:
            print('You will lose')
    else:
        print('You will lose')


get_bool_list(S, T)
get_false_index(bool_list)
win_or_lose(bool_list, false_index, S, T)
