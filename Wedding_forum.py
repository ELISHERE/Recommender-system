import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder
def weddingRecom():
    def preprocess_data(df):
        df['Civil_Marriage'].fillna('No', inplace=True)
        df['Civil_Partnership'].fillna('No', inplace=True)
        return df
    def recommend_wedding_venues(df, town, civil_status, civil_status1, k=5):
        filtered_df = df[(df['Town'] == town) & ((df['Civil_Marriage'] == civil_status) | (df['Civil_Partnership'] == civil_status1))]
        
        if filtered_df.empty:
            return "No recommended wedding venues found."
        if len(filtered_df) == 1:
            print(filtered_df[['Venue_Name', 'Contact_Number', 'Address', 'Website']])
            return []
        item_features = filtered_df[['Civil_Marriage', 'Civil_Partnership']]
        encoder = OneHotEncoder()
        item_features_encoded = encoder.fit_transform(item_features)
        item_similarity = cosine_similarity(item_features_encoded)
        venue_indices = item_similarity.argsort()[:, ::-1][:, 1:k+1]
        recommendations = []
        
        for indices in venue_indices:
            recommended_venues = filtered_df.iloc[indices][['Venue_Name', 'Contact_Number', 'Address', 'Website']]
            recommendations.append(recommended_venues)
        
        return recommendations
    df = pd.read_csv('Approved_Venues_for_Civil_Ceremonies_in_Causeway_Coast_and_Glens.csv')
    df = preprocess_data(df)
    town = input("Enter the town for the wedding venue: ")
    civil_status = input("Is civil marriage required? (Yes/No): ")
    civil_status1 = input("Is civil partnership required? (Yes/No): ")
    