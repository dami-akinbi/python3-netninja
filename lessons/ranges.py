# for n in range(5):
#     print(n)

# for t in range(3, 10):
#     print(t)

# for m in range(0, 20, 2):
#     if m == 0:
#         m += 1
#         continue
#     print(m)
#     if m == 16:
#         break

# burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']
# for n in range(len(burgers)):
#     print(f"{n} - {burgers[n]}")

burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']
for n in range(len(burgers) - 1, -1, -1):
    print(f"{n} - {burgers[n]}")
