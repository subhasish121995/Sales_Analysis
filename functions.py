def outliers(dataframe, column):
    import numpy as np
    Q1 = np.percentile(dataframe.column, 25)
    Q3 = np.percentile(dataframe.column, 75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5*IQR
    lower_bound = Q1 - 1.5*IQR
    outliers = dataframe.column[(dataframe.column > upper_bound)|(dataframe.column < lower_bound)]
    if len(outliers) == 0:
        return "There are no outliers in the data"
    else:
        return "The number of outliers that are present in the data are : ", len(outliers)

