import readItems
import updateItems
import generateInvoice


def operation(isCustomer):
    stocks = readItems.load()
    stocksList = []
    itemNames = []

    shoppedItems = []
    repeatedTransaction = False

    for i in stocks:
        itemNames.append(i.split(',')[0].lower())
        stocksList.append({"name": i.split(',')[0], "model": i.split(
            ',')[1], "price": int(i.split(',')[2].split('$')[1]), "quantity": int(i.split(',')[3])})
    continueTransaction = 'yes'
    name = input("Enter the name of the customer: ")
    lname = input("Enter the last name of the customer: ")
    while (continueTransaction.lower() == 'yes'):
        try:
            itemName = input(
                "Enter the item for Renting / returning : ")

            if (itemName.lower() not in itemNames):
                raise Exception('\nThere is no such item in our stock!')
            itemQuantity = int(
                input("Enter the quantity of the renting /returing product: "))

            if (len(shoppedItems) > 0):
                for item in shoppedItems:
                    if (item['name'].lower() == itemName.lower()):
                        raise Exception(
                            "You already have that item in the shopping cart!")

            for i in stocksList:
                if (i['name'].lower() == itemName.lower()):
                    if (isCustomer):
                        if (i['quantity'] < itemQuantity):
                            raise Exception(
                                "There aren't sufficient items in the stock!")

                    shoppedItems.append({'name': itemName.capitalize(), 'model': i['model'],
                                        'quantity': itemQuantity, 'price': i['price'], 'total': int(i['price'] * itemQuantity)})

                    # Removing or Adding items quantity from the shop too!
                    if (isCustomer):
                        i['quantity'] -= itemQuantity
                        shippingCost = int(input("Enter the shipping amount you want to charge to the customer: "))
                        generateInvoice.generateInvoice(isCustomer, name, shoppedItems, shippingCost)
                    else:
                        i['quantity'] += itemQuantity
                        generateInvoice.generateInvoice(isCustomer, name, shoppedItems)

        except Exception as err:
            print("\nSomething really went Wrong!!", err)
        finally:
            continueTransaction = input(
                "Do you again want to rent /return  the product? Type 'yes' for yes and type 'no' or anything to say no: ")

    updateItems.updateItems(stocksList)