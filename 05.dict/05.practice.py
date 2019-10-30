stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
    }

def displayInventory(inventory):
    print("Inventory")
    total = 0
    for k, v in inventory.items():
        total += v
        print('%d %s' % (v, k))
    print('Total number of items: %s' % total)

displayInventory(stuff)

print('--------------------------')

# 列表到字典的函数
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)