import pandas as pd

def rentRecom():
    df = pd.read_csv('House_Rent_Dataset.csv')
    user_price = int(input("Enter the price you want:"))
    user_size = int(input("Enter the size you want"))
    user_city = input("Enter Your City:")