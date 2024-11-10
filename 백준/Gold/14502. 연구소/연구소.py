from collections import deque
from itertools import combinations

def ms_BFS(graph, startings, max_x, max_y, visited):
    queue = deque()
    
    # 모든 시작점을 큐에 넣고 초기화
    for start_x, start_y in startings:
        queue.append((start_x, start_y))
        visited[start_x][start_y] = True

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        node_x, node_y = queue.popleft()
        
        for dir_x, dir_y in direction:
            next_x = node_x + dir_x
            next_y = node_y + dir_y
            
            if 0 <= next_x < max_x and 0 <= next_y < max_y:
                if graph[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

# 입력 처리
from sys import stdin
N, M = map(int, stdin.readline().rstrip().split())
maze = []
max_hap = 0

for _ in range(N):
    maze.append(list(map(int, stdin.readline().rstrip().split())))

startings = []
barrier_ok = []

# 시작 지점 수집
for y in range(N):
    for x in range(M):
        if maze[y][x] == 2:
            startings.append((y, x))
        elif maze[y][x] == 0:
            barrier_ok.append((y, x))

# 가능한 벽 3개 조합 탐색
for sources in combinations(barrier_ok, 3):
    visited = [[False] * M for _ in range(N)]

    # 벽을 설치
    for y, x in sources:
        maze[y][x] = 1

    # BFS 실행
    ms_BFS(maze, startings, N, M, visited)

    # 안전 영역 계산
    hap = sum(
        1 for y in range(N) for x in range(M) 
        if maze[y][x] == 0 and not visited[y][x]
    )

    max_hap = max(max_hap, hap)

    # 벽을 원래대로 복원
    for y, x in sources:
        maze[y][x] = 0

print(max_hap)