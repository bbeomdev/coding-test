import sys

n = int(sys.stdin.readline().strip())
num_list = {i: 0 for i in range(1, 10001)}
for i in range(n):
    num = int(sys.stdin.readline().strip())
    num_list[num] += 1
for i in num_list.keys():
    for i2 in range(num_list[i]):
        print(i)