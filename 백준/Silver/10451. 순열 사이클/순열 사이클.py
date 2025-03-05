def dfs(graph, dfs_visit, v):
    if dfs_visit[v] == True:
        return False
    dfs_visit[v] = True
    # print(f'방문노드 {v+1}')
    for i in graph[v]:
       if dfs_visit[i-1] == False:
           dfs(graph, dfs_visit, i-1)
    return True


n = int(input())
for _ in range(n):
    len_n = int(input())
    cycle_count = 0
    n_list = list(map(int, input().split()))
    graph = [[n_list[i]] for i in range(len_n)]
    dfs_visit = [False] * len_n
    for i in range(len(graph)):
        if dfs(graph, dfs_visit, i) == True:
            cycle_count += 1
            # print(cycle_count)
    print(cycle_count)