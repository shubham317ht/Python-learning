from sre_constants import RANGE


x = [value* 20 for value in range(1,5)]

# The code is creating a multiplication table from 1 to 10.

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')
