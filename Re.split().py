import re

string = input()

result = re.split(r'[.,]', string)

for i in result:
    print(i)
