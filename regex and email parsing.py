import re

# Regex for a valid email
pattern = re.compile(r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')

# Number of emails
n = int(input())

for _ in range(n):
    line = input().strip()
    
    # Parse the name and email
    name, email = line.split()
    
    # Remove < and > from email
    email_address = email[1:-1]
    
    # Validate email
    if pattern.match(email_address):
        print(line)
