import unittest
from PyDnD import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.newPlayer = Player(
            name="Thor Odinson",
            age="34",
            gender="Male",
            description="Looks like a pirate angel",
            biography="Born on Asgard, God of Thunder",
        )

    def test_description(self):
        # newPlayer is created, lets display some stats
        self.assertEqual("Thor Odinson", self.newPlayer.name)
        self.assertEqual("34", self.newPlayer.age)
        self.assertEqual("Male", self.newPlayer.gender)
        self.assertEqual("Looks like a pirate angel", self.newPlayer.description)
        self.assertEqual("Born on Asgard, God of Thunder", self.newPlayer.biography)

    def test_new_player_level(self):
        self.assertEqual(
            1, self.newPlayer.level
        )  # Level isn't specified in creation, so level is 1
        self.assertEqual(
            0, self.newPlayer.experience
        )  # Level wasn't specified, so current xp is 0
        self.assertEqual(
            1000, self.newPlayer.nextLvlExperience
        )  # 1000 Experience is required to get to level 2

    def test_level_up(self):
        self.newPlayer.giveExp(1000)
        self.assertEqual(
            1000, self.newPlayer.experience
        )  # Current, experience after leveling up
        self.assertEqual(
            2, self.newPlayer.level
        )  # newPlayer.level is automatically increased when XP threshold increases
        self.assertEqual(
            3000, self.newPlayer.nextLvlExperience
        )  # 3000 Experience is required to get to level 3


if __name__ == "__main__":
    unittest.main()
