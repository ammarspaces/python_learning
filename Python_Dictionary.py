movie = {
    'title':'Jumanji: The Next Level',
    'year' : 2017,
    'genre' : 'Adventure',
}

movie2 = {
    'title' : 'Frozen II',
    'year' : 2019,
    'genre' : 'Family',
}

print(movie['title'])

movie.update({'viewers': 44324578}) #Menambahkan item baru
movie["genre"] = "Adventure/Comedy" #Mengganti value dari key genre
del movie['year'] #Menghapus item year

print(movie)

# movie2.update({'viewers': 98698637})
# movie2['genre'] = "Family/Musical"
# print(movie2)