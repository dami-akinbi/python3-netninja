# function 2
def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        if num == 1:
            print(f"There is {num} {belt} belt")
        else:
            print(f"There are {num} {belt} belts")

# function 1
# def ninja_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f"I am {key} and I am a {val} belt")

ninja_belts = {}

while True:
    ninja_name = input('Enter a ninja name: ')
    ninja_belt = input('Enter a belt color: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? (y/n): ')
    if another == 'y':
        continue
    else:
        break

# result for function 1
# ninja_intro(ninja_belts)

# result for function 2
belt_count(ninja_belts)
