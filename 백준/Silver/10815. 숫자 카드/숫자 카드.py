import sys

case1 = int(sys.stdin.readline().rstrip())
target = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
case2 = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

for num in nums:
    
    start = 0
    end = case1 - 1
    exists = False

    while start <= end:
        mid = int((start + end) / 2)

        if target[mid] == num:
            exists = True
            break
        else:
            if target[mid] > num:
                end = mid - 1
            else:
                start = mid + 1
    
    if exists == True:
        print(1, end=' ')
    else:
        print(0 , end=' ')