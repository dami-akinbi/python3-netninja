# example
# def greet():
#     print('Hello, world!')
#
# greet()
# for i in range(4):
#     greet()


# example
# def greet(name = 'Ryu', time = 'morning'):
#     print(f"Good {time} {name}. Hope you are well?")

# name = input('Enter your name: ')
# time = input('Enter the time of day: ')

# greet(name, time)
# greet()
# greet('Joseph', 'afternoon')


# example
def area(radius):
    return 3.142 * radius * radius

def vol(area, length):
    print(area * length)

radius = int(input('Enter a radius: '))
length = int(input('Enter a length: '))

vol(area(radius), length)
