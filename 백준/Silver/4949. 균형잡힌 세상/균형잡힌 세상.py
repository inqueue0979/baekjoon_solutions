from sys import stdin
import re

while True:
    a = stdin.readline().rstrip()

    if a == '.':
        break

    a = re.sub(r"[a-zA-Z]", "", a).replace(' ', '').rstrip('.')

    while '()' in a or '[]' in a:
        a = a.replace('()','')  
        a = a.replace('[]','')

    if len(a) == 0:
        print('yes')
    else:
        print('no')