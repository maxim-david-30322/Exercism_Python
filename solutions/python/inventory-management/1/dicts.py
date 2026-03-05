"""Functions to keep track and alter inventory."""


def create_inventory(items):

    d={}    
    for w in items:
        d[w]=d.get(w,0)+1

    return d

    # for w in items:
    #     if w not in dic:
    #         dict[w,1]
    #     if w in dic:
    #         dic[w]=dic[w]+1
    
    # return dic
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    pass


def add_items(inventory, items):
    


    for w in items:
        inventory[w]=inventory.get(w,0)+1

    return inventory
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    pass


def decrement_items(inventory, items):

    for w in items:
        if w in inventory :
            if inventory.get(w,0)<=1:
                inventory[w]=0
            else:
                inventory[w]=inventory.get(w)-1

    return inventory
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    pass


def remove_item(inventory, item):

    inventory.pop(item,None)
    return inventory    

    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    pass


def list_inventory(inventory):

    inv=[]
    for word, nr in inventory.items():
        if nr!=0:
            inv.append((word, nr))
    return inv


    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    pass
