import pandas as pd

def sportRecom():
    def preprocess_data(df):
        df.fillna('Other', inplace=True)
        df.replace('Unknown', 'Other', inplace=True)
        return df
    df = pd.read_csv('Sports_Field_Fixtures.csv')
    df = preprocess_data(df)