name = ['josh','james','joe','jim']
# for i in name:
#     print(i)
[print(i) for i in name]

score = 90
print('A') if score >= 90 else print('B') if score >= 80 else print('C')

students_name = ['Alex','Bryan','Christ','Dave','Eva']
students_score = [100,75,80,78,99]
students_grade = []
students_grade = ['A' if i >=90 else
                  'B' if i >= 70 else
                  'C'
                  for i in students_score]
print(students_grade)

[print('I am learning python') for i in range(3)]