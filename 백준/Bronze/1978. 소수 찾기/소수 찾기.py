n = int(input())
num_list = [2,3,5,7,11,13,17,19,23,29,31]

num = list(map(int, input().split()))
num_count = 0

for i in num:
    num_count += 1
    if i == 1:
        num_count -= 1
        continue
    elif i in num_list:
        continue
    else:
        for i2 in num_list:
            if i % i2 == 0:
                num_count -= 1
                break
print(num_count)