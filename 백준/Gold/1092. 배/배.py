from sys import stdin

crane_amount = int(stdin.readline().rstrip())
crane_spec = sorted(list(map(int, stdin.readline().rstrip().split())), reverse=True)
box_amount = int(stdin.readline().rstrip())
box_weight = sorted(list(map(int, stdin.readline().rstrip().split())), reverse=True)
ans = 0
cursor_f, cursor_e = 0, box_amount

if box_weight[0] > crane_spec[0]:
    print(-1)
else:
    while box_weight:
        ans += 1
        for i in crane_spec:
            if box_weight and i < box_weight[-1]:
                continue
            for j in box_weight:
                if j <= i:
                    box_weight.remove(j)
                    break

    print(ans)