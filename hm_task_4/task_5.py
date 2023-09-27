import numpy as np


def matr_mul(n):
    list_mul = []
    for k in range(n - 1, 1, -1):
        if n % k == 0:
            list_mul.append(k)
    if len(list_mul) > 1:
        for i in range(len(list_mul) - 1):
            for j in range(i+1, len(list_mul)):
                matr_mul = np.random.randint(100, size=(list_mul[i], list_mul[j]),dtype=int)
                print(matr_mul)
                if list_mul[i] != list_mul[j]:
                    print(matr_mul.transpose())
    elif len(list_mul) == 1:
        print(np.random.randint(100, size=(list_mul[0], list_mul[0]), dtype=int))


matr_mul(12)