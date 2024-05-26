#3 užduotis
#	3.1 Apibrėžkite klasę Playlist su atributu songs (dainų pavadinimų sąrašas).
class Playlist:
    def __init__(self, songs: list) -> None:
        self.songs = songs
#	3.2 Pridėkite metodus add_song dainai į grojaraštį įtraukti, remove_song dainai pašalinti ir list_songs visoms grojaraščio dainoms grąžinti.
    def add_songs(self, song_name):
        if song_name not in self.songs:
            self.songs.append(song_name)
        else:
            print("Song already in list")

    def remove_song(self, song_name):
        if song_name in self.songs:
            self.songs.remove(song_name)
        else:
            print("No such song")

    def list_songs(self):
        return self.songs
#	3.3 Sukurkite grojaraščio objektą, pridėkite ir pašalinkite dainas ir atspausdinkite visų dainų sąrašą.

mato_pleilistas = Playlist(["Ay caramba","Du gaideliai","3 milijonai"])
print(mato_pleilistas.list_songs())
mato_pleilistas.add_songs("Cigono meile")
mato_pleilistas.remove_song("Du gaideliai")
print(mato_pleilistas.list_songs())
