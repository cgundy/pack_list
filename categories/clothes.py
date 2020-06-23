import math
from typing import Callable, Iterator, Union, Optional, List, Dict, Tuple
from categories.item import Item

class Clothes(Item):
    def adjust_quantity(self, quantity: int) -> int:
        if self.conditions['can_wash']:
            quantity = math.ceil(quantity / 2) + math.floor(quantity / 3)
        return quantity
    
class Jeans(Clothes):
    def get_quantity(self) -> int:
        if self.conditions['weather'] in ['cold','mild']:
            return math.ceil(self.conditions['days']/2)
        elif self.conditions['weather'] == 'hot':
            return math.ceil(self.conditions['days']/6)
        else:
            return 0

class Shirts(Clothes):
    def get_quantity(self) -> int:
        return self.conditions['days']

class Shorts(Clothes):
    def get_quantity(self) -> int:
        if self.conditions['weather'] == 'hot':
            return math.ceil(self.conditions['days']/2)
        else:
            return 0

class Dress(Clothes):
    def get_quantity(self) -> int:
        if self.conditions['weather'] == 'hot':
            return math.ceil(self.conditions['days']/4)
        else:
            return 0

class Underwear(Clothes):
    def get_quantity(self) -> int:
        return self.conditions['days']+2
