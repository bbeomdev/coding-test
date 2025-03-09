from collections import deque
n = int(input())
q = deque(list(range(1, n+1)))
while q:
    try:
        num1 = q.popleft()
        num2 = q.popleft()
    except:
        if n == 1:
            print(num1)
            break
        print(num2)
        break
    q.append(num2)