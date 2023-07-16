def DFS(graph, position, visited, direction, target, ranges):

    py, px = position
    visited[py][px] = True

    for dx, dy in direction:
        if 0 <= px + dx <= ranges - 1 and 0 <= py + dy <= ranges - 1:
            if graph[py + dy][px + dx] == target and visited[py + dy][px + dx] == False:
                DFS(graph, [py + dy, px + dx], visited, direction, target, ranges)


from sys import setrecursionlimit, stdin
setrecursionlimit(1000000000)

ranges = int(stdin.readline().rstrip())
normal_graph, rg_blind_graph = [], []
normal_ans, rg_ans = 0, 0
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for _ in range(ranges):
    line = stdin.readline().rstrip()
    normal_graph.append(line)
    rg_blind_graph.append(line.replace('G', 'R'))

normal_visited = [[False for _ in range(ranges)] for _ in range(ranges)]
rg_visited = [[False for _ in range(ranges)] for _ in range(ranges)]

#R DFS 돌림
for i in range(ranges):
    for j in range(ranges):
        if normal_graph[i][j] == 'R' and normal_visited[i][j] == False:
            DFS(normal_graph, [i, j], normal_visited, direction, 'R', ranges)
            normal_ans += 1
        
for i in range(ranges):
    for j in range(ranges):
        if rg_blind_graph[i][j] == 'R' and rg_visited[i][j] == False:
            DFS(rg_blind_graph, [i, j], rg_visited, direction, 'R', ranges)
            rg_ans += 1

#G DFS 돌림 (rg_blind는 생략해도 됨)
for i in range(ranges):
    for j in range(ranges):
        if normal_graph[i][j] == 'G' and normal_visited[i][j] == False:
            DFS(normal_graph, [i, j], normal_visited, direction, 'G', ranges)
            normal_ans += 1

#B DFS 돌림 (어차피 여기서부터는 같음)
for i in range(ranges):
    for j in range(ranges):
        if normal_graph[i][j] == 'B' and normal_visited[i][j] == False:
            DFS(normal_graph, [i, j], normal_visited, direction, 'B', ranges)
            normal_ans += 1
            rg_ans += 1

print(normal_ans, rg_ans)