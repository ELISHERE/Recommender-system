import pandas as pd

def hotelRecom():
    df = pd.read_csv('Hotel.csv', encoding='unicode_escape')
    location = input("Enter your preferred location: ")
    room_price = float(input("Enter your preferred room price: "))  # Convert input to float
    df['Room Price'] = df['Room Price'].str.replace('$', '', regex=True).str.strip()
    df['Room Price'] = pd.to_numeric(df['Room Price'], errors='coerce')