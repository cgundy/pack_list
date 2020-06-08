import math
from item import Item

class Clothes(Item):
    def adjust_quantity(self):
        raise NotImplementedError

class Underwear(Clothes):
    @staticmethod
    def get_quantity(conditions):
        return conditions['days']+2
    
class Jeans(Clothes):
    @staticmethod
    def get_quantity(conditions):
        if conditions['weather'] in ['cold','mild']:
            return math.ceil(conditions['days']/2)
        elif conditions['weather'] == 'hot':
            return math.ceil(conditions['days']/6)
        else:
            return 0