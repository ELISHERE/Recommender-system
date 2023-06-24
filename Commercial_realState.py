import re
import pandas as pd
def commercialRecom():
    def preprocess_price(price):
        if isinstance(price, str):
            numeric_part = re.findall(r'\d+\.?\d*', price)
            if numeric_part:
                price_value = float(numeric_part[0])
                if price_value.is_integer():
                    return int(price_value*1000)
                else:
                    return int(price_value * 1000000)
        return 0
    def preprocess_data(df):
        df['price'] = df['price'].apply(preprocess_price)
        df['area'] = df['area'].fillna(0).astype(str).str.extract(r'(\d+)', expand=False).astype(int)
        df['type'] = df['type'].fillna('Other')
        return df
    
    df = pd.read_csv('commercial_real_estate1.csv')
    df = preprocess_data(df)
    property_type = input("Enter the desired property type: ")
    price_range = input("Enter the desired price range (e.g., 100000-500000): ")
    area_range = input("Enter the desired area range (e.g., 500-1000): ")
    price_min, price_max = map(int, price_range.split('-'))
    area_min, area_max = map(int, area_range.split('-'))
    filtered_df = df[(df['type'].str.contains(property_type, case=False)) &
                    (df['price'].between(price_min, price_max)) &
                    (df['area'].between(area_min, area_max))]
    recommendations = filtered_df[['title', 'price', 'address', 'area', 'type']]
    for index, row in filtered_df.iterrows():
        print("Title:", row['title'])
        print("Price:", row['price'])
        print("Address:", row['address'])
        print("Area:", row['area'])
        print("Type:", row['type'])
        print("-" * 50)

    if filtered_df.empty:
        print("No recommended properties found.")