class Album:
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"
    
    def __repr__(self):
        return str(self)  

albums1 = [Album("Doolittle", "Pixies", 12),
    Album("Surfer Rosa", "Pixies", 15),
    Album("Bossanova", "Pixies", 20),
    Album("Trompe le Monde", "Pixies", 13),
    Album("Head Carrier", "Pixies", 18)]

print(f"Original albums1 list: {albums1}")  

albums1.sort(key = lambda album: album.number_of_songs) # key = lambda method indicating how to sort a list, in this case the key is number_of_songs
print(f"Sorted albums1 by number of songs: {albums1}")

albums1[0], albums1[1] = albums1[1], albums1[0]
print(f"Swap albums at position 1 [0] and 2[1]: {albums1}")

albums2 = [Album("No Need to Argue", "The Cranberries", 13),
    Album("Roses", "The Cranberries", 14),
    Album("Something Else", "The Cranberries", 20),
    Album("In The End", "The Cranberries", 18),
    Album("Everybody Else Is Doing It, So Why Can't We?", "The Cranberries", 15)]

print(f"Original albums2 list: {albums2}")  

albums2.extend(albums1)
print(f"First extended albums2 after adding albums1 to it: {albums2}")

albums2.extend([Album("Dark Side of the Moon", "Pink Floyd", 9),
    Album("Oops!... I Did It Again", "Britney Spears", 16)])

print(f"Second extended albums2 after adding two more albums to it: {albums2}")

albums2.sort(key = lambda album: album.album_name)  
print(f"Sorted albums2 by album title: {albums2}")

search_for = "Dark Side of the Moon"
search_index = 0
for index, album in enumerate(albums2):
    if album.album_name == search_for:
        search_index = index
        break

print(f"Found '{search_for}' at index {search_index}")
