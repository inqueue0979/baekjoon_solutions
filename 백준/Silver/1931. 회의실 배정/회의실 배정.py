from sys import stdin

cases = int(stdin.readline().rstrip())
elements = []
answer_list = {}
end_before, answer = 0, 0

for i in range(cases):
    a, b = map(int, stdin.readline().rstrip().split())
    elements.append([a, b])

elements = sorted(elements, key= lambda x : (x[1], x[0]))

for start_time, end_time in elements:
    if start_time >= end_before:
        answer += 1
        end_before = end_time

print(answer)