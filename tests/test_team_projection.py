import unittest
import team_projection as team

class testTeamProjection(unittest.TestCase):

    def testGetTeamName(self):
        parameters = {"team": "TOR"}
        teamName = team.getTeamName(parameters)
        self.assertEqual(teamName, "TOR")
