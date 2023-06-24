import pandas as pd
from scipy.spatial.distance import cosine

def rentRecom():
    def get_recommendations(user_price, user_size, user_city):
        filtered_df = df[df['City'] == user_city]
        filtered_df['similarity'] = filtered_df.apply(
            lambda row: 1 - cosine([user_price, user_size], [row['Rent'], row['Size']]),
            axis=1
        )
        filtered_df = filtered_df.sort_values('similarity', ascending=False)
        recommendations = filtered_df[['Rent', 'Size', 'City']].head(5)
        return recommendations
    df = pd.read_csv('House_Rent_Dataset.csv')
    user_price = int(input("Enter the price you want:"))
    user_size = int(input("Enter the size you want"))
    user_city = input("Enter Your City:")
    recommendations = get_recommendations(user_price, user_size, user_city)
    print(recommendations)