from typing import Dict, Union, Optional
class ResaleShop:
    
    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory, itemID):
        self.inventory: Dict[int, Dict[str, Union[str, int, bool]]] = {}
        self.itemID = 0
    
    def buy(self, computer: Dict[str, Union[str, int, bool]]):
        global itemID
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID    
    # buys and add the product to inventory
      
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[self.item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")   
    #updates the price according to the computer
            
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[self.item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
    #sells the product if available in the inventory        
        
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
        # For each item
            for item_id in self.inventory:
            # Print its details
                print('Item ID: {item_id} : {self.inventory[item_id]}')
        else:
                print("No inventory to display.")
    #prints the inventory

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if self.item_id in self.inventory:
            computer = inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                    computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                    computer["price"] = 250 # heavily-discounted price on machines 10+ years old
        elif int(computer["year_made"]) < 2018:
            computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer["price"] = 1000 # recent stuff

        if new_os is not None:
            computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.") 
    # updates the operating system if the computer has an old operating system