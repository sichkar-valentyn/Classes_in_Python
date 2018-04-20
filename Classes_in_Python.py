# Implementing the task
# Creating class MoneyBox
# Each instance of class MoneyBox supports only limited amount of money
# Class MoneyBox supports information about current amount of coins
# Also, gives information if it is possible to add more money
# And adds money

# Creating the class
class MoneyBox:
    # Constractor of the class
    def __init__(self, capacity):
        self.coins = 0
        self.count = capacity
    
    # Method to check the possibility to add more money
    def can_add(self, x):
        if self.coins + x <= self.count:
            return True
        else:
            return False
    
    # Method for adding more money
    def add(self, x):
        self.coins += x
        
