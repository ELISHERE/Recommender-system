import pandas as pd
def carsRecom():
    data = pd.read_csv('car_data.csv')
    selling_price = float(input("Enter selling price: "))
    kilometers_driven = float(input("Enter kilometers driven: "))
    year = int(input("Enter year: "))
    car_condition = float(input("Enter car condition (between 0 and 5): "))
    data['Similarity'] = (
        (data['Selling Price'] - selling_price) ** 2 +
        (data['Kilometers Driven'] - kilometers_driven) ** 2 +
        (data['Year'] - year) ** 2 +
        (data['Car Condition'] - car_condition) ** 2
    ) ** 0.5
    data = data.sort_values('Similarity')
    recommended_cars = data[['Model', 'Selling Price', 'Kilometers Driven', 'Year', 'Car Condition']].head(10)
    print("Recommended Cars:")
    print(recommended_cars)
