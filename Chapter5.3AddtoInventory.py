
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inv, loot):
    for item in loot:
        if item in inv.keys():
            inv[item] +=1
        else:
            inv[item] = 1
    return inv

startingInventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

newInventory = addToInventory(startingInventory, dragonLoot)
displayInventory(newInventory)