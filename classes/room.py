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

    def add_to_playlist(self, karaoke_bar, song):
        if song in karaoke_bar:
            self.playlist.append(song)
        else:
            return "song not available"

    def sing_song(self, song):
        self.playlist.remove(song)
