import sys
n = int(sys.stdin.readline().strip())
num = sys.stdin.readline().strip()
sum_num = 0
for i in range(n):
    sum_num += int(num[i]) 
print(sum_num)