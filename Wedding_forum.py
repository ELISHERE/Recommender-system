import pandas as pd
def weddingRecom():
    def preprocess_data(df):
        df['Civil_Marriage'].fillna('No', inplace=True)
        df['Civil_Partnership'].fillna('No', inplace=True)
        return df
    df = pd.read_csv('Approved_Venues_for_Civil_Ceremonies_in_Causeway_Coast_and_Glens.csv')
    df = preprocess_data(df)
    