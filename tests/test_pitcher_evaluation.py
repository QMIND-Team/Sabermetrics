import unittest
import pitcher_evaluation as pitch

class testPitcherEvaluation(unittest.TestCase):

    def testPitcherEvaluation(self):
        stats = ["release_speed"]
        dateRange = ["2017-04-01", "2017-04-02"]
        pitcherEval = pitch.pitcherEvaluation(573186, "", stats, dateRange, "", "")
        self.assertEqual(pitcherEval, 0)
