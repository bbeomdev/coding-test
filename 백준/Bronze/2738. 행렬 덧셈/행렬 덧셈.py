n,m = map(int, input().split())
a_list = [[0]*m for i in range(n)]
for i in range(2):
    for i2 in range(n):
        num_list = list(map(int, input().split()))
        for i3 in range(m):
            a_list[i2][i3] += num_list[i3]
for i in range(len(a_list)):
    print(' '.join(map(str, a_list[i])))