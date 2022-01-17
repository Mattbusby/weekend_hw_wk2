class Room:

    def __init__(self, room_name, guest_list, song_list, room_capacity):
        self.room_name = room_name
        self.guest_list = []
        self.song_list = []
        self.room_capacity = room_capacity

    def check_in_guest(self, guest):
        if self.room_capacity >= 1:
            if guest.wallet>=5:
                self.room_capacity -= 1
                self.guest_list.append(guest.name)
                guest.wallet -= 5
            else:
                return("You don't have enough cash to enter")
        else:
            return("This room is full")


    def check_out_guest(self, guest):
        self.guest_list.remove(guest.name)
        self.room_capacity += 1
        
    def add_song_to_room(self, song):
        self.song_list.append(song.song_name)
