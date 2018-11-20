import unittest
import team_projection as team

class TestTeamProjection(unittest.TestCase):

    def test_get_team_name(self):
        parameters = {"team": "TOR"}
        teamName = team.getTeamName(parameters)
        self.assertEqual(teamName, "TOR")