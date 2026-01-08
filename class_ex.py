class My_playlist:
    def __init__(self):
        self.myplaylist=[]

    def addPlaylist(self,song):
        self.myplaylist.append(song)
        print(f"Added {song}")

    def removePlaylist(self,song):
        self.myplaylist.remove(song)
        print(f"Removed {song}")

    def showPlaylist(self):
        print(self.myplaylist)

obj1 = My_playlist()
obj1.addPlaylist("Tujhe kitna ")
obj1.addPlaylist("Bekhayali...")
obj1.showPlaylist()
obj1.removePlaylist("Bekhayali...")
obj1.showPlaylist()

obj2 = My_playlist()
obj2.addPlaylist("Dekha aek khwab")
obj2.showPlaylist()