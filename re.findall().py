import re

s = input()

matches = re.finditer(r'(?<=[^AEIOUaeiou\W])([AEIOUaeiou]{2,})(?=[^AEIOUaeiou\W])', s)

found = False
for m in matches:
    print(m.group(1))
    found = True

if not found:
    print(-1)
