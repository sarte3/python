max_value = 0
a = 0
b = 0

for i in range(0, 101, 1):
    j = 100 - i

    if i * j > max_value:
        max_value = i*j
        a = i
        b = j
    else:
        continue

print('최대가 되는 경우 : {} * {} = {}'.format(a,b,max_value))