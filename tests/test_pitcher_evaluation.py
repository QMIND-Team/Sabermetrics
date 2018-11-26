import unittest
import pitcher_evaluation as pitch

class TestPitcherEvaluation(unittest.TestCase):

    def test_pitcher_evaluation(self):
        stats = ["release_speed"]
        dateRange = ["2017-04-01", "2017-04-02"]
        pitcher_eval = pitch.pitcherEvaluation(573186, "", stats, dateRange, "", "")
        self.assertEqual(pitcher_eval, 0)