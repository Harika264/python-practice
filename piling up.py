from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    cubes = deque(map(int, input().split()))

    last = float('inf')
    possible = True

    while cubes:
        left = cubes[0]
        right = cubes[-1]

        if left >= right and left <= last:
            last = cubes.popleft()
        elif right > left and right <= last:
            last = cubes.pop()
        else:
            possible = False
            break

    print("Yes" if possible else "No")
