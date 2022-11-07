# n, m, s = list(map(int, input().split()))
#
# left = []
# right = []

#
# for i in range(max(n, m)):
#     n_temp, m_temp = input().split()
#     left.append(int(n_temp)) if n_temp.isdigit() else left.append(0)
#     right.append(int(m_temp)) if m_temp.isdigit() else left.append(0)

n, m, s = list(map(int, input().split()))

lst = [i for _ in range(max(n, m)) for i in input().split()]
left = [int(i) if i.isdigit() else 0 for i in lst[::2] ]
right = [int(i) if i.isdigit() else 0 for i in lst[1::2]]


def get_list(stop_summa: int, lst: list) -> list:
    list_new = []
    summa = 0
    for index, number in enumerate(lst):
        summa += number
        if stop_summa >= summa:
            list_new.append((summa, index + 1))
        else:
            break
    return list_new


def get_count(lst1: list, lst2: list, stop_summa: int) -> int:
    tpl_end = lst1[-1]
    count = tpl_end[1]
    difference = stop_summa - tpl_end[0]

    if difference == 0:
        return count
    for i in range(len(lst2)):
        if lst2[-i - 1][0] <= difference:
            return count + lst2[-i - 1][1]
    return count


lst1 = get_list(s, left)
lst2 = get_list(s, right)

count1 = 0
if lst1:
    count1 = get_count(lst1, lst2, s)

count2 = 0
if lst2:
    count2 = get_count(lst2, lst1, s)

print(max(count1, count2))