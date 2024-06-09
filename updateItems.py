# File for updating stock items
def updateItems(stocksList):
    itemsFile = open('items.txt', 'w')
    for i in stocksList:
        itemsFile.write(
            f"{i['name'].capitalize()},{i['model'].capitalize()},${i['price']},{i['quantity']}")
        itemsFile.write("\n")
    itemsFile.close()