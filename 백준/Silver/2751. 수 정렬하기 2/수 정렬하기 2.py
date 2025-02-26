import sys
n = int(sys.stdin.readline())
sorted_num = sorted([int(sys.stdin.readline()) for _ in range(n)])
for i in sorted_num: print(i)