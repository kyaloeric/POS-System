def productsMenu():
    print("[1] Add product")
    print("[2] Delete product")
    print("[3] Modify product")
    print("[0] Exit")


# empty list to store added products
new_product = []

productsMenu()
option = int(input("Enter your option: "))
# perform specific operations based on entered choices
while option != 0:
    if option == 1:
        print(" Item will be added ")
        item = input("Enter a new item: ")
        new_product.append(item)
    elif option == 2:
        print("Deletion stuff will happen")
    elif option == 3:
        print("Modification  stuff will happen")

    elif option == 0:
        print("Exited successfully")
    else:
        print(" Invalid option")

    productsMenu()
    option = int(input("Enter your option: "))
print("Thanks for using the menu, Goodbye!!")
