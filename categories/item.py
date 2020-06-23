from typing import Callable, Iterator, Union, Optional, List, Dict, Tuple
from abc import abstractmethod
from typing_extensions import TypedDict

Conditions = TypedDict('Conditions', {'name': str, 'days': int, 'can_wash': bool, 'weather': str,
    'store_available': bool, 'outdoors': bool, 'downtime': bool, 'will_work': bool})

class Item:
    def __init__(self, conditions: Conditions):
        self.conditions = conditions
        
    @abstractmethod
    def get_quantity(self) -> int:
        raise NotImplementedError("Subclass must implement abstract method")
    
    @abstractmethod
    def adjust_quantity(self, quanitity: int) -> int:
        raise NotImplementedError("Subclass must implement abstract method")
