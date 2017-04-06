# viragenie for element in iterator
# list
number_list = [number-1 for number in range(1, 6)]
print(number_list)
print('------------------')

a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)
print('------------------')

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
print('------------------')

for row, col in cells:
    print(row, col)
print('------------------')

# dictionary
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
print('------------------')

# set
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)
print('------------------')

# generator
number_generator = (number for number in range(1, 6))
print(number_generator)
print(type(number_generator))
print('------------------')
