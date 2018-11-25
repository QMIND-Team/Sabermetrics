
def merge (d1,d2,on):

    newDF = pd.merge(d1,d2, on = [on], how ='outer')

    return newDF


