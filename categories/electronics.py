import math
from typing import Callable, Iterator, Union, Optional, List, Dict, Tuple
from categories.item import Item

class Electronics(Item):
    def adjust_quantity(self, quantity: int) -> int:
        if not self.conditions['store_available']:
            quantity += 1
        return quantity

class Ipad(Electronics):
    def get_quantity(self) -> int:
        if self.conditions['days'] <= 3 and self.conditions['downtime'] == False:
            return 1
        elif self.conditions['days'] > 5:
            return 1
        else:
            return 0

class Laptop(Electronics):
    def get_quantity(self) -> int:
        if self.conditions['days'] <= 3 and self.conditions['downtime'] == False:
            quantity = 0
        else:
            quantity = 1
        if self.conditions['will_work']:
            quantity += 1
        return quantity

class PhoneCharger(Electronics):
     def get_quantity(self) -> int:
        if self.conditions['days'] > 3:
            return 2
        else:
            return 1

class HeadPhones(Electronics):
    def get_quantity(self) -> int:
        if self.conditions['days'] > 5:
            quantity = 3
        else:
            quantity = 2
        if self.conditions['will_work']:
            quantity += 1
        return quantity
