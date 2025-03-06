from collections import deque


n,m = map(int, input().split())
graph = [[0] + list(map(int, input())) for _ in range(n)]
graph.insert(0, [0]+[0]*m)
bfs_visit = [[False] + [False] * m for _ in range(n)]
bfs_visit.insert(0, [False] + [False] * m)
first = (1,1)
q = deque()
q.append(first)
bfs_visit[1][1] = True
while q:
    x,y = q.popleft()
    graph_num = graph[x][y]
    try:
        if graph[x-1][y] != 0 and bfs_visit[x-1][y] == False:
            q.append((x-1,y))
            graph[x-1][y] += graph_num
            bfs_visit[x-1][y] = True
    except:
        pass

    try:
        if graph[x+1][y] != 0 and bfs_visit[x+1][y] == False:
            q.append((x+1,y))
            graph[x+1][y] += graph_num
            bfs_visit[x+1][y] = True
    except:
        pass

    try:
        if graph[x][y-1] != 0 and bfs_visit[x][y-1] == False:
            q.append((x,y-1))
            graph[x][y-1] += graph_num
            bfs_visit[x][y-1] = True
    except:
        pass

    try:
        if graph[x][y+1] != 0 and bfs_visit[x][y+1] == False:
            q.append((x,y+1))
            graph[x][y+1] += graph_num
            bfs_visit[x][y+1] = True
    except:
        pass

print(graph[n][m])