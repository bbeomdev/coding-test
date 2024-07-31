max_len = int(input())
for i in range(max_len):
    temp = list(map(int, input().split()))
    mean = sum(temp[1:]) / len(temp[1:])
    count = 0
    for sen_i in range(temp[0]):
        if temp[sen_i+1] > mean:
            count += 1
    print(f'{count / len(temp[1:]):.3%}')