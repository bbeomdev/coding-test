import sys
n = int(sys.stdin.readline().strip())
num_dict = {}
for i in range(n):
    num = int(sys.stdin.readline().strip())
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1
for i in sorted(num_dict.keys()):
    for i2 in range(num_dict[i]):
        print(i)