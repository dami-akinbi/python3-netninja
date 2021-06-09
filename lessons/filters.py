grades = ['A', 'B', 'F', 'C', 'F', 'A']

# filter method
# def remove_fails(grade):
#     return grade != 'F'
# print(list(filter(remove_fails, grades)))


# for loops method
# filtered_grades = []
# for grade in grades:
#     if grade != 'F':
#         filtered_grades.append(grade)
# print(filtered_grades)


# list comprehension method
filtered_grades = [ grade for grade in grades if grade != 'F' ]
print(filtered_grades)
