def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

d_add_ints = document_it(add_ints)
d_add_ints(5, 7)
print('-------------------------')

@document_it
def add_ints2(a, b):
    return a + b

add_ints2(6, 7)
print('-------------------------')