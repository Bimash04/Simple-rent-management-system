import readItems


def displayMenu():

    stocks = readItems.load()

    print('\n \t\t|~~~~~~~~~~~~~~~Welcome to the Rental Shop!!~~~~~~~~~~~~~~~|\n ||---------Please read the instructions carefully to proceed for further details---------||')
    for i in stocks:
        print("*********************************************************************************************************")
        print(
            f"EQUIPMENT NAME: {i.split(',')[0]} | BRAND: {i.split(',')[1]} | PRICE: {i.split(',')[2]} |  QUANTITY: {i.split(',')[3]}")

    print("*********************************************************************************************************")

    try:
        instruction = int(input(
            "Press 1: For renting please insert  or \nPress 2: For returing items to the customer: or \nPress any key: For exiting the program:  \n"))
        return instruction
    except:
        print("Please enter a valid instruction")
