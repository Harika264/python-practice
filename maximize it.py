# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

K, M = map(int, input().split())

lists = []
for _ in range(K):
    data = list(map(int, input().split()))
    lists.append(data[1:])

result = max(sum(x*x for x in combo) % M for combo in product(*lists))

print(result)
