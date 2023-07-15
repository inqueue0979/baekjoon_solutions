from collections import deque
from sys import stdin

def DFS(graph, root, visited):
    visited[root] = True
    print(root, end=' ')

    for j in graph[root]:
        if not visited[j]:
            DFS(graph, j, visited)

def BFS(graph, root):
    queue = deque()
    queue.append(root)
    visited = []

    while queue:
        val = queue.popleft()

        if not val in visited:
            visited.append(val)
            for j in graph[val]:
                queue.append(j)
    
    return visited

N, M, V = map(int, stdin.readline().rstrip().split())

graph_list = {}
visited = {}

for i in range(1, N + 1):
    graph_list[i] = []
    visited[i] = False

for j in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    graph_list[a].append(b)
    graph_list[b].append(a)

for k in range(1, N + 1):
    graph_list[k].sort()


DFS(graph_list, V, visited)
print()
print(*BFS(graph_list, V))