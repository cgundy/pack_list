class Item:
    def __init__(self, conditions):
        self.conditions = conditions
        
    def get_quantity(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def adjust_quantity(self):
        raise NotImplementedError("Subclass must implement abstract method")