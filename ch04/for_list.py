array = [273, 32, 103, 57, 52]

for element in array:
    print(element)

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for i in numbers:
    if(i%2==0):
        print(i, '는 짝수입니다')
    else:
        print(i, '는 홀수입니다')

for i in numbers:
    print(i,'는',len(str(i)), '자릿수입니다')

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for i in list_of_list:
    for j in i:
        print(j)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[],[],[]]

for number in numbers:
    output[(number+2)%3].append(number)

print(output)