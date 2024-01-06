# using recursion
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


print(fact(5))

# without using recursion


def fact2(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
