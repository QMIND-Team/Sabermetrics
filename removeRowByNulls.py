def removeRowsByNulls(df,threshold):
     length = df.shape[1]
     df = df.dropna(axis=0,thresh=length-threshold)
     return df



