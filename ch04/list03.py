list_a = [0, 1, 2, 3, 4, 5]
print('# 리스트의 요소 하나 제거하기')

del list_a[1]
print('del list_a[1] : ', list_a)

list_a.pop(2)
print('pop(2) : ', list_a)

list_a = [273, 32, 103, 57, 52]
print(273 in list_a)
print(99 in list_a)
print(100 in list_a)
print(52 in list_a)

print(273 not in list_a)
print(99 not in list_a)
print(100 not in list_a)
print(52 not in list_a)
