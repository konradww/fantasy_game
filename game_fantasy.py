inventory={
    'line': 1,
    'torch': 3,
    'gold coin': 142,
    'knife': 12,
    'arrow': 7
}

gift = ['gold coin', 'knife', 'gold coin', 'gold coin', 'ore']


def displayInventory(inventory):
    print("inventory:")
    itemTotal = 0
    for k, v in inventory.items():
        print (k, ':', v)
        itemTotal = inventory.get(k, 0) + itemTotal
    print('Total:', itemTotal)

def addToInventory(inventory, addedItems):
    count = 0
    for x in range(len(addedItems)):
        inventory.setdefault(addedItems[x], 0)  # create keys
        inventory[addedItems[x]] += 1
    return inventory

print(10 * '-----')
displayInventory(inventory)
print(10 * '-----')
addToInventory(inventory, gift)
displayInventory(inventory)
print(10 * '-----')








