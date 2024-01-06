# lambda is a anonymous functon which has no name
# the use lambda function is when we want function for a single call
# so we create a lambda function for single use and without name we create a function
# we use lambda to pass this function as argument to another function

# created lambda expression to hold it i used a variable
from turtle import towards


def twoMultiple(a): return a*2


# sourcery skip: use-fstring-for-formatting
print(f"{twoMultiple(1)} ", end="")
print(f"{twoMultiple(2)} ", end="")
print("{} {} {}".format(twoMultiple(3), twoMultiple(4), twoMultiple(5)), end="")
print(f" {twoMultiple(6)} {twoMultiple(7)} {twoMultiple(8)}", end="")


def even(a):
    return a % 2 == 0


def custom_filter(fun, arr):
    return [i for i in arr if fun(i)]


print(custom_filter(even, list(range(0, 20))))

print(custom_filter(lambda a: a%2!=0, list(range(20))))
