import re
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