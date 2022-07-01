class KaraokeBar:
    def __init__(self, _name, _till):
        self.name = _name
        self.till = _till
        self.song_book = []
        self.rooms = []

    def add_room_to_karaoke(self, room):
        self.rooms.append(room)

    # add the guest to the specified room if the room already exists and has space for entry
    def add_guest_to_room(self, room_to_enter, guest):
        if room_to_enter in self.rooms and room_to_enter.capacity > len(
            room_to_enter.guests
        ):
            room_to_enter.guests.append(guest)
        else:
            return "Room Full"
        return "room doesnt exist"

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
    
    # increases the kaaoke's till and decreases the guests wallet 
    def charge_entry_fee(self, guest):
        if guest.wallet >= 5:
            self.till += 5
            guest.wallet -= 5
        else:
            return "You do not have enough money to enter"

    # takes payment for the entry fee and adds the guest to the room specified
    def entry_into_room(self, room, guest):
        self.charge_entry_fee(guest)
        self.add_guest_to_room(room, guest)
