deg, dis = map(int, input().split())

x = deg * 10
y = round((dis / 60), 1)


dir_num = list(range(1125, 36001, 2250))
dir_name = [
        'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
        'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']

dic = dict(zip(dir_num, dir_name))

for i in range(len(dir_num)):
    if dir_num[i] <= x < dir_num[i+1]:
        Dir = dir_name[i]
        break
else:
    Dir = 'N'


wind_number = [
        0.0, 0.3, 1.6, 3.4, 5.5, 8.0, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7]


for i in range(len(wind_number)):
    if wind_number[i] <= y < wind_number[i+1]:
        W = i
        break
else:
    W = 12


if W == 0:
    Dir = 'C'


print(Dir, W)
