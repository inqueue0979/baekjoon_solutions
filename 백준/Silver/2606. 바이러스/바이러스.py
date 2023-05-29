from sys import stdin
from collections import deque

def bfs(graph, start):

    stack = deque([start])
    visited = []

    while stack:
        current = stack.popleft()
        if current not in visited:
            visited.append(current)
            stack += graph[current] - set(visited)
    
    return visited


graph = {}

for i in range(1, int(stdin.readline().rstrip()) + 1):
    graph[i] = set()

for _ in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].add(b)
    graph[b].add(a)

print(len(bfs(graph, 1)) - 1)