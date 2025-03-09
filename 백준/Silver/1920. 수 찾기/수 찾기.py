def binary(n_list, target, start, end):

    if start > end:
        return 0
    
    mid = int((start+end) / 2)
    if n_list[mid] == target:
        return 1
    
    elif n_list[mid] > target: # target이 mid보다 왼쪽에 있는경우
        return binary(n_list, target, start, mid-1)

    elif n_list[mid] < target: # target이 mid보다 오른쪽에 있는경우
        return binary(n_list, target, mid+1, end)


n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()

for i in m_list:
    result = binary(n_list, i, 0, n-1)
    print(result)