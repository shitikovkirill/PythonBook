import re

str='11 orders: OS141036916-0, OS141056549-0, OS141042201-0, OS141037239-0, OS141049695-0, OS141055579-0, OS141017877-0, OS141014534-0, OS141046822-0, OS141060594-0, OS141045775-0 '


regex = re.compile(r"(?<=:\s)(?P<orders_list>[\w-]*,?\s*){1,}")
list_of_orders = regex.search(str)
result = re.split('\s*,?\s+', list_of_orders.group(0))
print(result)

if __name__ == '__main__':
    pass