
def getFeatures(df ,features):
    return df[features]

def getTarget(df ,target):
    return df[target]

def get_numerical_data(df):
    return df._get_numeric_data()






