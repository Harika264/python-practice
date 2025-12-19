A = set(map(int, input().split()))
N = int(input())
result = True
for i in range(N):
    B = set(map(int, input().split()))
    if not A.issuperset(B) or A == B:
        result = False
        break
print(result)