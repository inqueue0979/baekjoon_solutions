import sys

def hap(cutter_height):
    sum = 0
    for tree_height in heights:
        if cutter_height <= tree_height:
            sum += tree_height - cutter_height
    
    return sum

N, M = map(int, sys.stdin.readline().rstrip().split())
heights = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

start = 0
end = heights[-1]
mid = 0
temp = 0

while start < end:
    mid = start + int((end-start) / 2)

    if hap(mid) > M:
        start = mid + 1
        temp = mid
    else:
        end = mid

if hap(end) < M:
    end = temp

print(end)