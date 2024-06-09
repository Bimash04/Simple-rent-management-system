import dateTime


def generateInvoice(isCustomer, name,  shoppingCart, shippingCost=0):
    totalAmount = 0
    if (isCustomer):
        fileName = f"Customer-{dateTime.dateTime}"
    else:
        fileName = f"Manufacturer-{dateTime.dateTime}"

    file = open(f"./invoices/{fileName}.txt", "w")

    file.write(
        "-------------------------------YOUR INVOICE-------------------------------")
    file.write("\n\n")
    file.write(
        f"Name: {name.capitalize()}                           Date:{dateTime.dateTime}")
    file.write("\n\n")
    for i in shoppingCart:
        totalAmount += i['total']
        file.write(
            f"Item: {i['name']} - Model: {i['model']} X {i['quantity']} pcs -> Price: ${i['price']}")
        file.write('\n')

    # if (isCustomer):
    #     file.write(f"Total amount without shippingCost: ${totalAmount}\n")
    #     file.write(f"Shipping Cost: ${shippingCost}\n")
    #     file.write('________________________________\n')
    #     file.write(f"Total Amount: ${totalAmount + shippingCost}")
    # else:
    #     file.write(f"Total amount without VAT: ${totalAmount}\n")
    #     file.write(
    #         f"VAT (13%) AMOUNT: ${(13/100)*totalAmount}\n")
    #     file.write('________________________________\n')
    #     file.write(
    #         f"Total Amount: ${totalAmount + ((13/100)*totalAmount)}")
    file.write("\n\n")
    file.write(
        "-------------------------------THANK YOU!! Visit Again!!-------------------------------")
    file.close()