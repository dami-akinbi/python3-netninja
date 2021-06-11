with open('files/write.txt', 'w') as write_file:
    write_file.write("Hey there buddy. Python is cool!")

# junk

with open('files/write.txt', 'a') as write_file:
    write_file.write("\nYou would find it very relevant in Data Science.")

quotes = [
    '\nI can resist everything except temptation',
    '\nWe are all in the gutter, but some of us are looking at the stars',
    '\nAlways forgive your enemies - nothing annoys them so much'
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)
