def load():
    file = open("./items.txt", "r")
    items = [item.replace('\n', ' ') for item in file.readlines()]
    itemsArray = []
    for item in items:
        itemsArray.append(item)

    return itemsArray
