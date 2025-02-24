import sys
n = int(sys.stdin.readline().strip())
n_i = 0
num = 0
while True:
    num += 1
    if str(num).find('666') != -1:
        n_i += 1
    if n_i == n:
        print(num)
        break
    