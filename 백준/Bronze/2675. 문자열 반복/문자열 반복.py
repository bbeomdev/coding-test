n = int(input())
for i in range(n):
    s = input().split()
    s_list = []
    for s_i in s[1]:
        s_list.append(s_i*int(s[0]))
    print(''.join(s_list))