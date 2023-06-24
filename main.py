from Wedding_forum import weddingRecom
from Commercial_realState import commercialRecom
while(True):
    print("1.Wedding forum recommendation system")
    print("2.Commercial real state recommendation system")
    print("0.Exit")
    menu = int(input("Enter the menu number:"))
    if menu == 1:
        weddingRecom()
    elif menu == 2:
        commercialRecom()
    elif menu == 0:
        break