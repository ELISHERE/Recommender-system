from Wedding_forum import weddingRecom
from Commercial_realState import commercialRecom
from Sports_field import sportRecom
from hotel import hotelRecom
from car import carsRecom
from houseRent import rentRecom
while(True):
    print("1.Wedding forum recommendation system")
    print("2.Commercial real state recommendation system")
    print("3.Sport field recommendation system")
    print("4.Hotel recommendation system")
    print("5.Car recommendation system")
    print("6.House renting recommendation system")
    print("0.Exit")
    menu = int(input("Enter the menu number:"))
    if menu == 1:
        weddingRecom()
    elif menu == 2:
        commercialRecom()
    elif menu == 3:
        sportRecom()
    elif menu == 4:
        hotelRecom()
    elif menu == 5:
        carsRecom()
    elif menu == 6:
        rentRecom()
    elif menu == 0:
        break