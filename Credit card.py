import re

n = int(input())

for _ in range(n):
    card = input().strip()

    # Regex for valid card format
    pattern = r'^[4-6]\d{3}(-?\d{4}){3}$'

    # Check basic format
    if not re.match(pattern, card):
        print("Invalid")
        continue

    # Remove hyphens to check repeated digits
    clean_card = card.replace('-', '')

    # Check for 4 or more consecutive repeated digits
    if re.search(r'(\d)\1{3,}', clean_card):
        print("Invalid")
    else:
        print("Valid")
