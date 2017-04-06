def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

print(type(my_range))
print(type(my_range(1, 6)))
ranger = my_range(1, 8)
for x in ranger:
    print(x)
