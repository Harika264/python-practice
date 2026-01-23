import re

n = int(input())

for _ in range(n):
    uid = input().strip()

    if (
        len(uid) == 10
        and uid.isalnum()
        and len(set(uid)) == 10
        and re.search(r'[A-Z].*[A-Z]', uid)
        and re.search(r'\d.*\d.*\d', uid)
    ):
        print("Valid")
    else:
        print("Invalid")
