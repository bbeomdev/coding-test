n = int(input())
n_i = -1
for i in range(n+1):
    st_i = str(i)
    temp = i + sum(int(st_i[n_i]) for n_i in range(len(st_i)))
    if temp == n:
        n_i = i
        print(n_i)
        break
if n_i == -1:
    print(0)