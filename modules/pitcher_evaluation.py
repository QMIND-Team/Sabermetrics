import data_query

def pitcherEvaluation(pitcherId, teamName, stats, dateRange, league, aggregate):
    df = data_query.query(pitcherId, teamName, stats, dateRange, league, aggregate)
    return 0
