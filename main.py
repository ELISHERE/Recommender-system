from Wedding_forum import weddingRecom
while(True):
    print("1.Wedding forum recommendation system")
    print("0.Exit")
    menu = int(input("Enter the menu number:"))
    if menu == 1:
        weddingRecom()
    elif menu == 0:
        break