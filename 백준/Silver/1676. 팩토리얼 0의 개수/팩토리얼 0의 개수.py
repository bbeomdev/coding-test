import sys
n = int(input())
num = 1
for i in range(1, n+1):
    num *= i
for i, str_i in enumerate(str(num)[::-1]):
    if str_i != '0':
        print(i)
        break