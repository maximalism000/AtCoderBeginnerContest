m = float(input())
km = m * 10 ** (-3)

if km < 0.1:
    vv = 0
elif 0.1 <= km <= 5.0:
    vv = 10 * km
elif 6 <= km <= 30:
    vv = km + 50
elif 35 <= km <= 70:
    vv = (km - 30) / 5 + 80
elif km >= 70:
    vv = 89


if vv < 10:
    x = '0%d' % int(vv)
else:
    x = int(vv)


print(x)
