import pandas as pd

def sportRecom():
    def preprocess_data(df):
        df.fillna('Other', inplace=True)
        df.replace('Unknown', 'Other', inplace=True)
        return df
    
    df = pd.read_csv('Sports_Field_Fixtures.csv')
    df = preprocess_data(df)
    user_type = input("Enter the type of sport ground you are looking for: ")
    user_material = input("Enter the material preference: ")
    user_owner = input("Enter the owner preference: ")