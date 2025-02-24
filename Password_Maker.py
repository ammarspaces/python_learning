import random
import string

print("Welcome to Password Maker!")

adjectives_list = ["sleepy","slow","fluffy","red","yellow","green","blue"]
nouns_list = ["Dinosaur","Ball","Dragon","Hammer","Apple","Duck","Panda"]

#Kumpulan variabel untuk mengacak kata sifat, kata benda, angka, dan karakter spesial
adjective = random.choice(adjectives_list)
noun = random.choice(nouns_list)
number = random.randrange(0,100)
char = random.choice(string.punctuation)

#Kombinasi untuk menghasilkan password
password = adjective + noun + str(number) + char
print("Recommended password: " + password)

