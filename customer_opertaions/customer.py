# customer menu options
from customer_opertaions.add_customer import add_customer


def customerMenu():
    print("*********************************")
    print(" KINDLY MAKE A CHOICE TO CONTINUE")
    print("*********************************")
    print("1. Insert customer.")
    print("2. Update customer.")
    print("3. Delete customer.")
    print("0. Exit.")


def customer_main():
    customerMenu()
    choice = int(input("Enter your choice: "))

    while True:
        if choice == "1":
            print(" A customer is going to be inserted")
            add_customer()
        elif choice == "2":
            print("A customer is going to be updated")
        elif choice == "3":
            print("A customer is going to be deleted")
        elif choice == "0":
            print("Exiting")
        else:
            print(" Oops!! Wrong choice!!")

        customer_main()
