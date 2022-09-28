from product_operatons.add_product import add_product
from customer_opertaions.add_customer import add_customer

def menu():
    print("******************************")
    print("WELCOME TO ROCKS HOTEL MENU ")
    print("******************************")
    print("[1] Handle customers")
    print("[2] Handle products")
    print("[3] Handle queries")
    print("[0] Exit")
    menu()


choice = int(input("Enter your option: "))


def main():
    global choice
    while choice != 0:
        if choice == 1:
            add_customer()
        elif choice == 2:
            print("Handle products")
            add_product()
        elif choice == 0:
            print("Exited successfully")
        else:
            print(" Invalid option")

        choice = int(input("Enter your option: "))

        menu()

        print("Thanks for using the menu, Goodbye!!")


if __name__ == '__main__':
    main()
