from sys import stdin

num = int(stdin.readline().rstrip())
find_num = int(stdin.readline().rstrip())
arr = [[0 for i in range(num)] for j in range(num)]

loc_x, loc_y = num // 2, num // 2
loc = [[0,-1], [1,0], [0,1], [-1,0]]
addition = 2
fill = 0
ans = [0, 0]

while fill <= num * num:
    for x, y in loc:
        for _ in range(addition // 2):
            fill += 1
            if loc_x >= 0 and loc_x <= num and loc_y >= 0 and loc_y <= num:
                arr[loc_y][loc_x] = fill
                if fill == find_num:
                    ans = [loc_y + 1, loc_x + 1]
                loc_y += y
                loc_x += x
        addition += 1

for i in arr:
    print(*i)
print(ans[0], ans[1])