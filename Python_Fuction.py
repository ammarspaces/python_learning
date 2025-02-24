number = [10,16,30,21]
# print(max(number)) #Menampilkan nilai yang paling besar
# print(min(number)) #Menampilkan nilai yang paling kecil
# print("hello".upper()) #Mengubah teks menjadi huruf kapital
# print("WELCOME".lower()) #Mengubah teks menjadi huruf kecil

# def order_pizza():
#     quantity = 1
#     price = 10
#     total_order = quantity * price
#     print(f"Total order $: {total_order}")

# order_pizza()

# def order_pizza(quantity):
#     price = 10
#     total_order = quantity * price
#     print(f"Total order $: {total_order}")

# order_pizza(7)

total = 100 #Global variable
def sum():
    first = 10
    second = 20
    total = first+second #Local variable
    print(total)
print(total)

sum()