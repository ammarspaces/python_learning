# allowance = 10
# spending = 8
# print(allowance < spending)
# print(allowance > spending)
# print(allowance != spending)
# print(allowance == spending)


# print((allowance == 10) and (spending == 8))

# print((allowance == 12) or (spending == 8))

# students_name = ['Alex','Bryan','Christ','Dave','Eva']
# students_score = [100,75,80,78,99]
# students_grade = []

# for i in students_score:
#     if(i >= 90):
#         students_grade.append('A') #Menambahkan nilai pada list
#     elif(i >= 70):
#         students_grade.append('B')
#     else:
#         students_grade.append('C')
# print(students_grade)

#Conditional Loop

while True:
    answer = input("""Do you  want to loop this argument?
    Type yes or no: """)
    if answer.lower() == "yes": #lower() merupakan perintah dari python untuk membuat string menjadi lowercase
        print("Okay let's go!")
    else:
        print("Good bye...")
        break

