import time


# problem_1


def message1(text_list):
    corr_text = text_list.split()
    stop_list = ["Python", "php", "go", "C"]
    corr_text = ''.join(list(filter(lambda x: x not in stop_list, corr_text)))

    return corr_text


text_list1 = "asdasd Python php asdfsfd yhl,rl go Cjgf;a"
print(message1(text_list1))


# problem_2


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def multipl(n):
    global list1
    return list(filter(lambda x: x % n == 0, list1))


print(multipl(3))


# problem_3


def add(*args):
    value = []

    for item in args:
        if isinstance(item, str):
            value.append(item)

    return tuple(value)


total = add(1, "function", 2, 3, 4, "Python", 5.0, "kwargs")
print(total)


# problem_4


def intersec(list2, list3):
    inter_list = list2
    inter_list = list(filter(lambda x: x in list3, inter_list))

    return inter_list


total1 = [1, 7, "function", 3.0, 12, "Python", 5.0, "kwargs", "abc"]
total2 = [1, "functions", 2, 3, 4, "Python", 5.0, "kwargs"]
print(intersec(total1, total2))


# problem_5

cnt = 0


def lesenka(lev, n):
    global cnt
    for i in range(lev, n + 1):
        lesenka(i + 1, n - i)
    if n == 0:
        cnt += 1


lesenka(1, 6)
print(cnt)

# problem_6


def decor1(fn):
    def wrapp1(*args):
        res = fn(*args)
        if not isinstance(res, int):
            raise Exception("Тип введенной переменной отличный от int")
        else:
            return f'Результат вычислений: {res}'

    return wrapp1


@decor1
def square(n):
    return n ** 2


@decor1
def mult(m):
    return m * 2


print(square(3))
#print(mult("str"))


# problem_7


def decor2(fn):
    def wrapp2(*args):
        try:
            return fn(*args)
        except:
            str1 = input("Enter the string: ")
            return fn(str1)

    return wrapp2


@decor2
def length_string(s: str) -> int:
    n = len(s)
    return n


s1: str = "abc"
print(length_string(s1))


@decor2
def str_up(s: str) -> str:
    return s.upper()

str2 = "abc"
print(str_up(str2))


# problem_8


elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]

print(sorted(elements, key=lambda elements: elements[1]))


# problem_9


def decor3(fn):
    def wrapp3(*args):
        start_time = time.time()
        code_to_test = fn(*args)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return f'Elapsed time: {elapsed_time}, result: {code_to_test}'

    return wrapp3


@decor3
def my_sqrt(n):
    return n ** 0.5


@decor3
def sort_list(list4: list):
    return sorted(list4, key=lambda list4: list1[1])


print(my_sqrt(0.25))
print(sort_list(elements))
