my_name = 'Ryu'

def print_name():
    global my_name
    my_name = 'Yoshi'
    print(f"The name inside the function is {my_name}")

print_name()
print(f"The name outside the function is {my_name}")
