max_len = int(input())
for i in range(max_len):
    ox = input()
    index = 0
    score = 0
    for st in ox:
        if st == 'O':
            index += 1
            score += index
        if st == 'X':
            index = 0
    print(score)