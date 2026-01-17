from collections import deque

for _ in range(int(input())):
    n = int(input())
    d = deque(map(int, input().split()))
    last = float('inf')
    for _ in range(n):
        if d[0] >= d[-1] and d[0] <= last:
            last = d.popleft()
        elif d[-1] <= last:
            last = d.pop()
        else:
            print("No")
            break
    else:
        print("Yes")
