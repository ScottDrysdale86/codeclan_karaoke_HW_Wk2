class Room:
    def __init__(self, _room_name, _capacity):
        self.room_name = _room_name
        self.capacity = _capacity
        self.guests = []
        self.playlist = []

    def check_capacity(self):
        return self.capacity

    def check_guests_in_room(self):
        return len(self.guests)

    def add_to_playlist(self, karaoke_bar_songbook, song_to_add):
        if song_to_add in karaoke_bar_songbook:
            self.playlist.append(song_to_add)
        else:
            return "song not available"

    def sing_song(self, song):
        self.playlist.remove(song)

    def check_favourite_song_in_playlist(self, guest):
        for song in self.playlist:
            if guest.fav_song == song.title:
                return "Woo Hoo, I love this song"
