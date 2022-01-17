import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 =  Room("Disco", [], [], 10)
        self.room_2 =  Room("Hiphop", [], [], 10)
        self.room_3 =  Room("Rap", [], [], 0)
        # rooms = [self.room_1, self.room_2, self.room_3]
        self.song_1 = Song("Everything in it's right place")
        self.song_2 = Song("Kid A")
        # songs = [self.song_1, self.song_2]
        self.guest_1 = Guest("Bill", 10)
        self.guest_2 = Guest("Joe", 5)
        self.guest_3 = Guest("Sam", 0)
        # guests = [self.guest_1, self.guest_2, self.guest_3]
        
    def test_room_has_name(self):
        self.assertEqual("Disco", self.room_1.room_name)

    def test_check_in_guest(self):
        self.assertEqual(0, len(self.room_1.guest_list))
        Room.check_in_guest(self.room_1, self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))

    def test_check_out_guest(self):
        Room.check_in_guest(self.room_1, self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))
        Room.check_out_guest(self.room_1, self.guest_1)
        self.assertEqual(0, len(self.room_1.guest_list))

    def test_add_song_to_room(self):
        Room.add_song_to_room(self.room_1, self.song_2)
        self.assertEqual(1, len(self.room_1.song_list))

    def test_check_room_has_space(self):
        Room.check_in_guest(self.room_2, self.guest_2)
        self.assertEqual(9, self.room_2.room_capacity)
        self.assertEqual("This room is full", Room.check_in_guest(self.room_3, self.guest_1))

    def test_customers_pay_entry_fee(self):
        Room.check_in_guest(self.room_2, self.guest_2)
        self.assertEqual(0, self.guest_2.wallet)
        self.assertEqual("You don't have enough cash to enter", Room.check_in_guest(self.room_2, self.guest_3))


    # def test_increase_till(self):
    #     self.Room.increase_till(2.50)
    #     self.assertEqual(102.50, self.Room.till)