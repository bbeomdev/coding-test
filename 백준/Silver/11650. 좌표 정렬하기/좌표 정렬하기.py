import sys

# n = int(input())
n = int(sys.stdin.readline().strip())
coord = {}
for i in range(n):
    # x, y = map(int, input().split())
    x,y = map(int, sys.stdin.readline().strip().split())
    if x not in coord:
        coord[x] = []
        coord[x].append(y)
    else:
        coord[x].append(y)

for i in sorted(coord.keys()):
    for i2 in sorted(coord[i]):
        print(i, i2)