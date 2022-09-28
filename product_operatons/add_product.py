def add_product():
    foo = open("pos-cli.txt", "a+")
    prod_name = input("Enter the product name: ")
    mfg_date = input(" Enter manufacturing date: ")
    serial_number = int(input("Enter the serial number: "))
    foo.write(str(mfg_date) + prod_name + " " + str(serial_number) + "\n")  # new line
    foo.close()


add_product()
