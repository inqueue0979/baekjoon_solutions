from sys import stdin

ratings = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

rating_sum = 0
rating_count = 0

for i in range(20):
    name, amount, rating = stdin.readline().rstrip().split()
    if rating != 'P':
        rating_sum += float(amount) * ratings[rating]
        rating_count += float(amount)

print('%.8f' % (rating_sum / rating_count))