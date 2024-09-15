from sys import stdin
data = stdin.readline().rstrip()
temp = ''
in_tag = False

for datum in data:
    if datum == ' ' and in_tag == False:
        print(temp[::-1], end=' ')
        temp = ''
    elif datum == '<':
        in_tag = True
        print(temp[::-1], end='')
        temp = ''
    elif datum == '>':
        in_tag = False
        print('<' + temp, end='>')
        temp = ''
    else:
        temp += datum

print(temp[::-1])