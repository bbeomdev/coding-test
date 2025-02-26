import sys
n = int(sys.stdin.readline().strip())
in_data = [sys.stdin.readline().strip().split() for _ in range(n)]
in_data = sorted(in_data, key = lambda x: int(x[0]))
for i in in_data: print(' '.join(i))