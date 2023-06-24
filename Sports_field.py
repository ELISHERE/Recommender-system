import pandas as pd
from sklearn.neighbors import NearestNeighbors

def sportRecom():
    def preprocess_data(df):
        df.fillna('Other', inplace=True)
        df.replace('Unknown', 'Other', inplace=True)
        return df
    def recommend_sport_ground(df, user_type, user_material, user_owner, k=5):
        filtered_df = df[(df['TYPE'] == user_type) | (df['MATERIAL'] == user_material) | (df['OWNER'] == user_owner)]
        if filtered_df.empty:
            return "No similar sport grounds found."
        features = filtered_df[['TYPE', 'MATERIAL', 'OWNER']]
        combined_data = pd.concat([features, pd.DataFrame({'TYPE': [user_type],
                                                        'MATERIAL': [user_material],
                                                        'OWNER': [user_owner]})])
        combined_encoded = pd.get_dummies(combined_data)
        features_encoded = combined_encoded[:-1]
        user_preferences = combined_encoded[-1:]
        model = NearestNeighbors(n_neighbors=k)
        model.fit(features_encoded)
        distances, indices = model.kneighbors(user_preferences)
        recommended_indices = indices.squeeze()
        return filtered_df.iloc[recommended_indices][['TYPE', 'MATERIAL', 'OWNER', 'POINT']]
    
    df = pd.read_csv('Sports_Field_Fixtures.csv')
    df = preprocess_data(df)
    user_type = input("Enter the type of sport ground you are looking for: ")
    user_material = input("Enter the material preference: ")
    user_owner = input("Enter the owner preference: ")
    recommendations = recommend_sport_ground(df, user_type, user_material, user_owner)
    print(recommendations)