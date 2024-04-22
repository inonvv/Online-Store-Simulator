from Classes.StoreInventory import StoreInventory


class Store:
    def __init__(self, store_inventory=None, costumers=None):
        if store_inventory is None:
            store_inventory = StoreInventory()
        self.store_inventory = store_inventory
        if costumers is None:
            costumers = []
        self.costumers = costumers
