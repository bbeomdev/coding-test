a = list(map(int, input().split()))
b = list(map(int, input().split()))
sen = []
for num in range(a[0]):
    if a[1] > b[num]:
        print(b[num], end=" ")