N = int(input())

table = [1]
for i in range(2, N+1):
    table.append(i * table[i-2])
print(table[-1])