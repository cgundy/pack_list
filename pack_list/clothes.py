import math
from item import Item

class Clothes(Item):

    def adjust_quantity(self, quantity):
        if self.conditions['can_wash']:
            quantity = math.ceil(quantity / 2) + math.floor(quantity / 3)
        return quantity

class Underwear(Clothes):
    def get_quantity(self):
        return self.conditions['days']+2
    
class Jeans(Clothes):
    def get_quantity(self):
        if self.conditions['weather'] in ['cold','mild']:
            return math.ceil(self.conditions['days']/2)
        elif self.conditions['weather'] == 'hot':
            return math.ceil(self.conditions['days']/6)
        else:
            return 0