def knights(saying):
    def inner():
        return '-- %s --' % saying
    return inner

a = knights('Duck')
b = knights('Dgek')

print(type(a))
print(type(a))

print(a)
print(a)

print(a())
print(b())
