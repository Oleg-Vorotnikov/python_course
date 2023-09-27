import numpy as np

# problem 1

my_arr = np.random.randint(100, size=10, dtype=int)
my_arr.sort()
print(my_arr)

# problem 2

x1 = np.ones(64).reshape((8, 8))

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                x1[i, j] = 0
        else:
            if j % 2 == 1:
                x1[i, j] = 0

print(x1)

# problem_3

matr1 = np.random.randint(10, size=(8, 4), dtype=int)
matr2 = np.random.randint(10, size=(4, 2), dtype=int)
print(np.dot(matr1, matr2))

# problem_4

x2 = np.linspace(0, 1, 12)[1:-1]
print(x2)

