import unittest
from PyDnD import RollStats


class TestStatRoller(unittest.TestCase):
    def test_roll_standard_ability_scores(self):
        # test standard ability score rolling
        def roll():
            roller = RollStats()
            roller.stat_roller()
            return roller.statroll

        scores = [roll() for _ in range(6)]
        self.assertEqual(len(scores), 6)
        for score in scores:
            self.assertGreaterEqual(score, 3)
            self.assertLessEqual(score, 18)

    def test_roll_classic_ability_scores(self):
        # test classic ability score rolling
        def roll():
            roller = RollStats("classic")
            roller.stat_roller()
            return roller.statroll

        scores = [roll() for _ in range(6)]
        self.assertEqual(len(scores), 6)
        for score in scores:
            self.assertGreaterEqual(score, 3)
            self.assertLessEqual(score, 18)

    def test_roll_heroic_ability_scores(self):
        # test standard ability score rolling
        def roll():
            roller = RollStats("heroic")
            roller.stat_roller()
            return roller.statroll

        scores = [roll() for _ in range(6)]
        self.assertEqual(len(scores), 6)
        for score in scores:
            self.assertGreaterEqual(score, 3)
            self.assertLessEqual(score, 18)


if __name__ == "__main__":
    unittest.main()
