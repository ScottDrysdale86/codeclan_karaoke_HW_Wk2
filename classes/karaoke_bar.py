class KaraokeBar:
    def __init__(self, _name, _till):
        self.name = _name
        self.till = _till
        self.song_book = []
        self.rooms = []

    def add_room_to_karaoke(self, room):
        self.rooms.append(room)

    def add_guest_to_room(self, room, guest):
        if room in self.rooms and room.capacity > len(room.guests):
            room.guests.append(guest)
        else:
            return "Room Full"

    def remove_from_room(self, room, guest):
        if room in self.rooms:
            room.guests.remove(guest)

    def add_to_song_book(self, song):
        self.song_book.append(song)

    def remove_from_song_book(self, song):
        if song in self.song_book:
            self.song_book.remove(song)
        else:
            return "Song is not in songbook"

    def charge_entry_fee(self, guest):
        self.till += 5
        guest.wallet -= 5
    
