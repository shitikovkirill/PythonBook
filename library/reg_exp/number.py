import re

prog = re.compile(r"(^\d*)-[0-9]{3}-[0-9]{3}")
print(prog)
result = prog.match('10874955-000-060')
print(result.group(1))
print('-----------------------')

result = re.match('You', 'Young Frankenstain Young')
print(result.group())
print('-----------------------')

result = re.search('You', 'Young Frankenstain Young')
print(result.group())
print('-----------------------')

result = re.findall('You', 'Young Frankenstain Young')
print(result)
print('-----------------------')

result = re.findall('You', 'Young Frankenstain Young')
print(result)
print('-----------------------')

result = re.split('n', 'Young Frankenstain Young')
print(result)
print('-----------------------')

result = re.sub('n', '?', 'Young Frankenstain Young')
print(result)
print('-----------------------')

result = re.search(r'(Young) (Moung)', 'Young Moung')
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.groups())
print('-----------------------')

result = re.search(r'(?P<one>Young) (?P<two>Moung)', 'Young Moung')
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group())
print(result.group('one'))
print(result.group('two'))
print('-----------------------')
if __name__ == '__main__':
    pass