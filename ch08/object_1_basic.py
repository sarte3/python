students = [
    {'name': '윤인성', 'korean': 87, 'math':98, 'english':88, 'science':95},
    {'name': '연하진', 'korean': 92, 'math':98, 'english':96, 'science':98}

]

print('이름', '총점', '평균', sep='\t')
for student in students:
    score_sum = student['korean'] + student['math'] + student['english'] + student['science']
    score_average = score_sum / 4

    print(student['name'], score_sum, score_average, sep='\t')