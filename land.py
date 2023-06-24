import pandas as pd
import numpy as np
def landsRecom():    
    lands_data = pd.read_csv('land.csv')
    lands_data['land_size'].fillna(0, inplace=True)
    city = input("Enter the city: ")
    land_size = float(input("Enter the land size: "))
    price = float(input("Enter the price: "))