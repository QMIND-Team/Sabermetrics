import unittest
from tests.test_pitcher_evaluation import TestPitcherEvaluation
from tests.test_team_projection import TestTeamProjection
from tests.test_data_query import TestDataQuery

suiteTeam = unittest.makeSuite(TestTeamProjection)
suitePitch = unittest.makeSuite(TestPitcherEvaluation)
suiteQuery = unittest.makeSuite(TestDataQuery)

allTests = unittest.TestSuite((suiteTeam, suitePitch, suiteQuery))
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(allTests)