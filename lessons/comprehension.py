# double prize money weekend bonanza
prizes = [5, 10, 50, 100, 1000]

# normal method
# double_prizes = []
# for prize in prizes:
#     double_prizes.append(prize * 2)
#
# print()
# print('Double Prizes:')
# print(double_prizes)

# comprehension method
double_prizes = [ prize * 2 for prize in prizes ]
print()
print('Double Prizes:')
print(double_prizes)

# squaring method
nums = [1,2,3,4,5,6,7,8,9,10]

# normal method
# squared_even_nums = []
# for num in nums:
#     if (num ** 2) % 2 == 0:
#         squared_even_nums.append(num ** 2)
# print()
# print('Squared Even Numbers:')
# print(squared_even_nums)

# comprehension method
squared_even_nums = [ num ** 2 for num in nums if num % 2 == 0 ]
print()
print('Squared Even Numbers:')
print(squared_even_nums)
