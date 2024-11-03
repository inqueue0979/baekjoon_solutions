from sys import stdin
from itertools import combinations

N, M = map(int, stdin.readline().rstrip().split())
letters = sorted(list(stdin.readline().rstrip().split()))
moeum_list = 'aeiou'
dictionary = dict()

for combination in combinations(letters, N):
    moeum = sum(1 for c in combination if c in moeum_list)
    jaeum = N - moeum
    
    if moeum >= 1 and jaeum >= 2:
        result = ''.join(combination)
        if not dictionary.get(result):
            print(result)
            dictionary[result] = 1