from sys import stdin

K, N = map(int, stdin.readline().rstrip().split())
lan = [int(stdin.readline().rstrip()) for _ in range(K)]
lan.sort()

answer = 0
start = 0
end = lan[-1]

while start <= end:
    mid = (start + end) // 2
    hap = 0

    if mid == 0:
        answer = 1
        break

    for i in lan:
        hap += (i // mid)
    
    if hap >= N:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
    

print(answer)