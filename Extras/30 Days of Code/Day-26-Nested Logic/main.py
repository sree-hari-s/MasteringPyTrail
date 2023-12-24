date_returned = list(map(int, input().split()))
d1, m1, y1 = date_returned
date_expected = list(map(int, input().split()))
d2, m2, y2 = date_expected

fine = 0

if y1>y2:
    fine = 10000
elif y1 == y2:
    if m1 > m2:
        fine = (m1-m2)*500
    elif m1 == m2 and d1 > d2:
        fine = (d1-d2)*15

print(fine)