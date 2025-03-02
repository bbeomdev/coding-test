n = int(input())
num_list = list(map(int, input().split()))
max_num = max(num_list)
for i in range(n):
    num_list[i] = (num_list[i] / max_num) * 100
print(sum(num_list) / len(num_list))