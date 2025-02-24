grocery_list = ['Bread','Cereal','Peanut Butter']
print(grocery_list)

# print(grocery_list[0]) #menampilkan data pertama
# print(grocery_list[1]) #menampilkan data ke-2

# print(grocery_list[-1]) #menampilkan data terakhir

grocery_list.append('Sausage') #Menambahkan item pada list

# grocery_list.append('Croissant')

print(grocery_list)

grocery_list.remove ('Bread') #Menghapus item pada list

print(grocery_list)

grocery_list[1] = 'Strawberry Jam' #Mengubah item indeks ke 1
print(grocery_list) 
print(len(grocery_list)) #Menampilkan jumlah item pada list

numbers = [130,100,140,150,190,200,250,200,230,250]

numbers.sort()
print(numbers)
grade_3 = numbers[:5] #Mengambil item sebelum index ke 4
print(grade_3)

grade_2 = numbers[4:7] #Mengurutkan item pada list menjadi urutan kecil ke besar
print(grade_2)

grade_1 = numbers[7:] #Mengambil item setelah index ke 7
print(grade_1)

# ages = [14,15,8,10,17,18,20,21,19,10,25,21,10,20,15]

# ages.sort()

# new_ages = ages[7:]

# print(new_ages)

temperature = [
    [25,27,28,27],
    [23,24,26,26],
    [24,24,27,27],
    [22,24,25,24]
]

print(temperature[0])
print(temperature[3][2])
print(temperature[0][0])

# temperature.append([23,24,24,26])
# temperature.append([23,24,24])
# print(temperature)
# print(len(temperature))
# temperature[1][2] = 27

# print(temperature)
