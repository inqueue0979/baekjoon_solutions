def DFS(graph, position, visited, width, height):

    direction = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]
    py, px = position
    visited[py][px] = True

    for dx, dy in direction:
        if 0 <= px + dx <= width - 1 and 0 <= py + dy <= height - 1:
            if graph[py + dy][px + dx] == '1' and visited[py + dy][px + dx] == False:
                DFS(graph, [py + dy, px + dx], visited, width, height)


from sys import setrecursionlimit, stdin
setrecursionlimit(1000000)

while True:
    width, height = map(int, stdin.readline().rstrip().split())

    if width == 0 and height == 0:
        break

    visited = [[False for _ in range(width)] for _ in range(height)]
    graph = []
    answer = 0

    for _ in range(height):
        graph.append(stdin.readline().rstrip().split())


    for i in range(height):
        for j in range(width):
            
            if graph[i][j] == '1' and visited[i][j] == False:
                DFS(graph, [i, j], visited, width, height)
                answer += 1

    print(answer)