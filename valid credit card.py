import re

n = int(input())

for _ in range(n):
    card = input().strip()

    # Check basic format
    pattern = r'^(4|5|6)\d{3}(-?\d{4}){3}$'
    if not re.match(pattern, card):
        print("Invalid")
        continue

    # Remove hyphens for repetition check
    card_digits = card.replace('-', '')

    # Check for 4 or more consecutive repeated digits
    if re.search(r'(\d)\1{3,}', card_digits):
        print("Invalid")
    else:
        print("Valid")
