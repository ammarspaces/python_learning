import discord
import random

sad_words = ["sad","depressed","angry","hurting","stressed"]

encouragements = [
    "Cheer up!",
    "Hang in there ",
    "You are a great person!",
    "Come on you can do it!",
    "Stay strong!"
]

intents = discord.Intents.default()
intents.message_content = True #Konfigurasi agar pesan dari client dapat dibaca
client = discord.Client(intents=intents) #Membuat koneksi antara klien dengan discord. Kelas Client digunakan untuk berinteraksi dengan discord.




@client.event #Me-registrasi event, akan ada banyak event diddalamnya.
async def on_ready(): #menangani event-event ketika klien sudah terkoneksi dengan discord.
    print("We have logged in as {0.user}"
                   .format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user: #Memastikan bahwa kita mengabaikan pesan dari diri sendiri
        return
    if message.content.startswith('!hi'): #Jika mengirimkan !hi maka bot akan mengirim pesan halo
        await message.channel.send(f'Hello ☺️')
    if message.content.startswith('!hello'):
        await message.channel.send('https://media.giphy.com/media/6Zu8A0iogHglFXJXB2/giphy.gif')
    if any(word in message.content for word in sad_words): #Jika mengirimkan kalimat yang berisi kata pada list sad_words
        response = random.choice(encouragements) #Pilih satu item pada list encouragements sebagai respon
        await message.channel.send(response)

client.run("<token>")