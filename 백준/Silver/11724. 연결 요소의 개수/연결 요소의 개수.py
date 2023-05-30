from sys import stdin
from collections import deque

def bfs(graph, length):

    visited = []
    not_visited = [i for i in range(1, length + 1)]
    stack = deque([1])
    bundle = 0

    while not_visited:

        while stack:
            current = stack.popleft()
            if current not in visited:
                visited.append(current)
                stack += graph[current] - set(visited)
                not_visited = list(set(not_visited) - set(visited))

        bundle += 1
        
        if not_visited:
            stack = deque([not_visited[0]])
    
    return bundle


graph = {}

N, M = map(int, stdin.readline().rstrip().split())

for i in range(1, N + 1):
    graph[i] = set()

for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].add(b)
    graph[b].add(a)

print(bfs(graph, N))