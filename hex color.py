import re

n = int(input())

pattern = r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?'

for _ in range(n):
    line = input()
    
    # Ignore selectors
    if line.strip().startswith('#'):
        continue

    matches = re.findall(pattern, line)
    for m in matches:
        print(m)
