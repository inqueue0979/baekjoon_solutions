from sys import stdin

data = list(stdin.readline().rstrip())
temp = 1
ans = 0
stack = []

for i in range(len(data)):
    if data[i] == '(':
        temp *= 2
        stack.append('(')

    elif data[i] == ')':

        if not len(stack) or stack[-1] != '(':
            ans = 0
            break
        elif data[i-1] == '(':
            ans += temp
            temp //= 2
            stack.pop()
        else:
            temp //= 2
            stack.pop()

    elif data[i] == '[':
        temp *= 3
        stack.append('[')

    elif data[i] == ']':

        if not len(stack) or stack[-1] != '[':
            ans = 0
            break
        elif data[i-1] == '[':
            ans += temp
            temp //= 3
            stack.pop()
        else:
            temp //= 3
            stack.pop()

if len(stack): ans = 0

print(ans)