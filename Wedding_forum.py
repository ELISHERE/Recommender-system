import pandas as pd
def weddingRecom():
    def preprocess_data(df):
        df['Civil_Marriage'].fillna('No', inplace=True)
        df['Civil_Partnership'].fillna('No', inplace=True)
        return df
    df = pd.read_csv('Approved_Venues_for_Civil_Ceremonies_in_Causeway_Coast_and_Glens.csv')
    df = preprocess_data(df)
    town = input("Enter the town for the wedding venue: ")
    civil_status = input("Is civil marriage required? (Yes/No): ")
    civil_status1 = input("Is civil partnership required? (Yes/No): ")
    