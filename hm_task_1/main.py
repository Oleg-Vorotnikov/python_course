# problem_1

def length_string(s: str) -> int:
    n = len(s)
    return n


s1: str = ""
print(length_string(s1))


# problem_2


def comp_len(l1: list, l2: list):
    if len(l1) > len(l2):
        return len(l1)
    elif len(l1) < len(l2):
        return len(l2)
    else:
        return "Equal"


l11 = [1, 5, 13, 34, 3]
l22 = ['ddf', 2, 3]
print(comp_len(l11, l22))


# problem_3


def list_append(test_list, t):
    test_list.append(t)
    return test_list


test_list1 = [3, 4, 2, 4]
t1 = 1
print(list_append(test_list1, t1))


# problem_4


def numb_interval(n):
    if n in range(-100, 101):
        return '+'
    else:
        return '-'


n1 = 100
print(numb_interval(n1))


# problem_5


def find_str(str_1, str_2):
    if str_1 in str_2:
        print('Yes')
    else:
        print('No')


str_1 = 'test'
str_2 = 'test1'
find_str(str_1, str_2)


# problem_6


def count_positive(numb_list):
    cnt = 0
    for i in range(len(numb_list)):
        if numb_list[i] > 0:
            cnt += 1
    return cnt


numb_list1 = [1, -7, 0, 24, -1, 13]
print(count_positive(numb_list1))


# problem_7


def numb_days(years, month):
    days = (years * 12 + month) * 29
    return days


years1 = 5
month1 = 7
print(numb_days(years1, month1))


# problem_8


def abbrev(text: str):
    abbr = ''
    if text[0] != ' ':
        abbr += text[0]
    for i in range(len(text) - 1):
        if text[i] == ' ' and text[i + 1] != ' ':
            abbr += text[i + 1]
    return abbr


text1 = ' s df dsjn njajffee e'
#text1 = 5
try:
    print(abbrev(text1))
except:
    print('Неверный ввод')


# problem_9


def factorial(f: int):
    n = f
    m = 1
    while n > 1:
        m *= n
        n -= 1
    return m


nm = 6
print(factorial(nm))


# problem_10


lst = [2, 4, 5, 8, 9, 13]
number = 0

while number < len(lst):
    lst[number] *= number
    number += 1
print(lst)
