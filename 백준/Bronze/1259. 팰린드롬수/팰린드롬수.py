import sys
# st = sys.stdin.readline().strip()
while True:
    st = input()
    if st == '0':
        break
    elif st == st[::-1]:
        print('yes')
    else:
        print('no')