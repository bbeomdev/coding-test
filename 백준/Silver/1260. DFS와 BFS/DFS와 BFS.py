from collections import deque
def dfs(graph, dfs_visit, v):
    dfs_visit[v] = True # 맨처음 v 정점을 방문 체크
    print(v, end=' ')
    for i in graph[v]: # v 주변 연결된 노드들 꺼내서
        if dfs_visit[i] == False: # 방문 안 되어있으면
            dfs(graph, dfs_visit, i) # 끝까지 내려감


def bfs(graph, bfs_visit, v):
    q = deque()
    q.append(v) # 맨처음 시작 노드를 큐에 넣고
    bfs_visit[v] = True
    bfs_list = []
    while q: # q가 끝날때까지 반복
        v = q.popleft() # # 큐에서 v를 뽑음
        print(v, end=' ')
        for i in graph[v]: # 그 v 근처 연결된 노드들 큐에 넣어야됨
            if bfs_visit[i] == False: # 방문 안 되어있으면
                q.append(i)
                bfs_visit[i] = True
    

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
dfs_visit = [False] * (n+1)
bfs_visit = [False] * (n+1)
for i in range(m):
    in_n, in_m = map(int, input().split())
    graph[in_n].append(in_m)
    graph[in_m].append(in_n)
graph = list(map(lambda x: sorted(x), graph))
dfs(graph, dfs_visit, v)
print('')
bfs(graph, bfs_visit, v)