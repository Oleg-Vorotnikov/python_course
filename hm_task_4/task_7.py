import numpy
import numpy as np


def oper_arr(A: numpy.ndarray, S: int, last=False):        # А как задать аннотацию к массиву?
    X = A.shape[0]
    #B = np.random.randint(15, size=(S, X), dtype=int)
    B = np.random.random((S, X))
    A2 = A * B
    list_sum = []
    for i in range(A2.shape[0]):
        sum_str = sum(A2[i, ::1])
        list_sum.append(sum_str)
    S1 = np.array(list_sum, float)
    if not last:
        S1 = np.sin(S1)
    else:
        S1 = np.maximum(S1, 0)
    return B, S1


vec1 = np.random.randint(20, size=5, dtype=int)

#vec1 = np.random.random(5)

# print(oper_arr(vec1, 10))
vec2 = oper_arr(vec1, 10)[1]

vec3 = oper_arr(vec2, 10)[1]

B, S1 = oper_arr(vec3, 5, True)
print(S1 * 100)
# не очень какие должны быть случайные величины и что значит вернуть процент