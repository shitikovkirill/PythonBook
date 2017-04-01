import re

prog = re.compile(r"(^\d*)-[0-9]{3}-[0-9]{3}")
result = prog.match('10874955-000-060')
print result.group(1)