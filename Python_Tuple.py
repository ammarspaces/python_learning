subjects = ("Python","C++","Javascript")
# # print(subjects)
# # print(len(subjects))
# subjek = ("C++")

# print(subjects[-1]) #Print indeks terakhir
# print(subjects[1]) #Print indeks kedua
# print(subjects[0:2]) #Print indeks ke nol dan kedua

# print("Python" in subjects) #Cek apakah python ada di tuple
# print("Java" in subjects) #Cek apakah java ada di tuple

# subjects[1] = "Mathlab"
# print(subjects[1]) #TypeError: 'tuple' object does not support item assignment

#Unpact tuples
subject1,subject2,subject3 = subjects
# print(subject1)
# print(subject2)
# print(subject3)
subjek = (subject2)
subjek[0] = "Mathlab"
print(subjek)