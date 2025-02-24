import random

score = 0
player_name = input("Please enter your name: ")

while True:
    #Memilih 1 kata pada list secara acak dan menyimpannya pada variable pick
    words = ["Python","Computer","Programming",
             "Condition","Else","Break","Input",
             "Print","While","For"]
    pick = random.choice(words)
    #Mengacak huruf pada kata yang telah dipilih pada variable pick, lalu menampilkan hasil kata acak pada console untuk ditebak
    random_word = random.sample(pick,len(pick))
    jumbled = "".join(random_word)
    print("Jumbled word is :", jumbled)

    answer = input("what is in your mind? ")
    #Mengecek jawaban user, jika jawaban user sama dengan kata yang dipilih pada variable pick maka user mendapat 1 point
    if answer == pick:
        score += 1
        print("Your score is :", score)
        #Jika user berhasil menjawab 10 pertanyaan dengan benar maka user memenangkan game
        if score == 10:
            print("Congratulation ",player_name, "you win!")
            print("Your score is :", score)
            break
        #Jika user salah menebak jawaban maka sistem akan memberi tahu jawaban yang benar dan user diberi pilihan untuk melanjutkan game atau berhenti
    else:
        print("Better luck next time... correct word is :", pick)
        cont = input("press 'y' to continue and 'n' to quit : ")
        if cont == "n":
            print(player_name, "Your score is :",score)
            print("Thanks for playing...")
            break
        