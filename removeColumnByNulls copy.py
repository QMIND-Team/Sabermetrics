
def removeColumnsByNulls(df,threshold):
     length = df.shape[0]
     df = df.dropna(axis=1,thresh=length-threshold)
     return df

