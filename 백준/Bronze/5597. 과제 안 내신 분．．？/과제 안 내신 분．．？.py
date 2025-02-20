all_num=list(range(1,31))
for i in range(28):
    num = int(input())
    all_num.remove(num)
all_num = sorted(all_num)
print(all_num[0])
print(all_num[1])