a, b = 0, 1
while b < 1000:
    str = b.__str__() + ','
    print str
    a, b = b, a+b

print '-------------'

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

print '-------------'

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print words

print '-------------'

for i in range(5):
    print(i)

print '-------------'

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print '-------------'

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            #loop fell through without finding a factor
            print(n, 'is a prime number')

print '-------------'

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

print '-------------'

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print '-------------'

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print '-------------'

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

r = zip(questions, answers)
print r

for q, a in r:
    print('What is your {0}?  It is {1}.'.format(q, a))