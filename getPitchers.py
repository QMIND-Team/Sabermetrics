
def getTeamPitchingRoster(teamName):
    player = []
    data = pitching()
    df = pd.DataFrame(data)

    length = df.shape[0]

    df = df[df.teamID.str.contains(teamName)]
    return df

