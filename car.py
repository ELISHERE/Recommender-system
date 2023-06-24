import pandas as pd
def carsRecom():
    data = pd.read_csv('car_data.csv')
    selling_price = float(input("Enter selling price: "))
    kilometers_driven = float(input("Enter kilometers driven: "))
    year = int(input("Enter year: "))
    car_condition = float(input("Enter car condition (between 0 and 5): "))
    
