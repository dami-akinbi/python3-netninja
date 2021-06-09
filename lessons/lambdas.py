nums = [1, 2, 3, 4, 5, 6]

# named function method
# def square(n):
#     return n * n
# print(list(map(square, nums)))


# a lambda is an anonymous function
# lambdas are inline functions
# lambda function method
print(list(map(lambda n: n * n, nums)))
