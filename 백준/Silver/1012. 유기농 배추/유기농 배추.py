def DFS(graph, points, point, visited, direction):
    #print(point)
    visited.append(point)
    points.remove(point)

    for x, y in direction:
        try:
            a = graph[point[0] + y][point[1] + x]
            if a == 1 and [point[0] + y, point[1] + x] not in visited:
                #print('vis', str(a), str([point[0] + y, point[1] + x]), str(visited))
                n_point = [point[0] + y, point[1] + x]
                DFS(graph, points, n_point, visited, direction)
        except:
            pass


import sys
from sys import stdin
sys.setrecursionlimit(10000)

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
points = list()

for _ in range(int(stdin.readline().rstrip())):
    M, N, K = map(int, stdin.readline().rstrip().split())

    answer = 0
    visited = []
    graph = [[0 for i in range(M)] for j in range(N)]

    for _ in range(K):
        x, y = map(int, stdin.readline().rstrip().split())
        points.append([y, x])
        graph[y][x] = 1
    
    #print(points)

    while points:
        DFS(graph, points, points[0], visited, direction)
        #print(str(answer) + '번')
        answer += 1
    

    print(answer)