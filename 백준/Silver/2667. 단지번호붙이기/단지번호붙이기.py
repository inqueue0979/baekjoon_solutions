def DFS(graph, position, visited, direction):
    visited.append(position)

    for x, y in direction:
        if 0 <= position[0] + y <= len(graph) - 1 and 0 <= position[1] + x <= len(graph) - 1:
            if graph[position[0] + y][position[1] + x] == '1' and [position[0] + y, position[1] + x] not in visited:
                DFS(graph, [position[0] + y, position[1] + x], visited, direction)


from sys import setrecursionlimit, stdin

setrecursionlimit(10000)
graph = []
visited = []
ans_1 = 0
ans_2 = []
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

length = int(stdin.readline().rstrip())

for i in range(1, length + 1):
    graph.append(stdin.readline().rstrip())

for i in range(length):
    for j in range(length):
        
        if (graph[i][j] == '1') and (not [i,j] in visited):
            DFS(graph, [i,j], visited, direction)
            ans_1 += 1
        
            ans_2.append(len(visited) - sum(ans_2))

print(ans_1)
ans_2.sort()
for i in ans_2:
    print(i)