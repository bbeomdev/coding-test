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
direct = [(-1,0), (1,0), (0,-1), (0,1)]

while q:
    x,y = q.popleft()
    graph_num = graph[x][y]
    for dx, dy in direct:
        try:
            if graph[x+dx][y+dy] != 0 and bfs_visit[x+dx][y+dy] == False:
                q.append((x+dx,y+dy))
                graph[x+dx][y+dy] += graph_num
                bfs_visit[x+dx][y+dy] = True
        except:
            pass

print(graph[n][m])