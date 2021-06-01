""" A Helper Module for commonly used functions in Lambdata """ 
""" This function cleans the df of all outliers """
def rm_outlier(df):
    filepath = input(df)
    df = pd.read_csv("filepath")
    return df 


""" This function reformats MM/DD/YYYY into separate series """
def split_dates(date_series = pd.Series):
    #TODO - Implement 
    pass 
