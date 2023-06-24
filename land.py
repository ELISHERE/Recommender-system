import pandas as pd
import numpy as np
def landsRecom():   
    def recommend_lands(city, land_size, price):
        filtered_lands = lands_data[lands_data['city'] == city]
        normalized_data = filtered_lands[['land_size', 'price']].apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
        feature_matrix = normalized_data.values
        test_land = [(land_size - np.min(normalized_data['land_size'])) / (np.max(normalized_data['land_size']) - np.min(normalized_data['land_size'])),
                    (price - np.min(normalized_data['price'])) / (np.max(normalized_data['price']) - np.min(normalized_data['price']))]
        distances = np.sqrt(np.sum((feature_matrix - test_land) ** 2, axis=1))
        sorted_indices = np.argsort(distances)
        k = 10  
        nearest_indices = sorted_indices[:k]
        recommendations = filtered_lands.iloc[nearest_indices]
        return recommendations
 
    lands_data = pd.read_csv('land.csv')
    lands_data['land_size'].fillna(0, inplace=True)
    city = input("Enter the city: ")
    land_size = float(input("Enter the land size: "))
    price = float(input("Enter the price: "))
    recommended_lands = recommend_lands(city, land_size, price)
    print("Recommended lands:")
    print(recommended_lands)