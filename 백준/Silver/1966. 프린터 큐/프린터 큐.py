from collections import deque

test_i = int(input())
for _ in range(test_i):
    q = deque()
    n, m = map(int, input().split())
    q_list = list(map(int, input().split()))
    q.extend(q_list)

    q_count = 0
    temp_count = 0
    max_num = max(q)
    while q:
        pop_num = q.popleft()
        # print(f'pop_num {pop_num}, q_count {q_count}, temp_count {temp_count}, m {m}')

        if pop_num != max_num: # 꺼낸값이 최대값과 같지 않으면
            if temp_count == m: # 만약 우리가 찾던 값이면 
                m = len(q) # 찾던 값의 인덱스를 업데이트하고
                temp_count = 0 # 큐 인덱스도 초기화
                q.append(pop_num)
                continue
            else:
                q.append(pop_num)
                temp_count += 1
                continue
            
        elif pop_num == max_num: # 꺼낸값이 최대값과 같으면
            q_count += 1 # 출력 횟수를 1 올리고
            if temp_count == m: # 만약 우리가 찾던 값이면
                print(q_count) # 이때까지 출력 횟수를 print하고 반복문 종료
                break
            max_num = max(q) # 바뀐 큐의 최대값을 업데이트함
            temp_count += 1