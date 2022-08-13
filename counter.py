import datetime
from datetime import date
from user import User

"""
Counter class: 
Responsible for calculating:
    - Remaining Time
    - Spent Time
"""

class Counter:
    """
    Calculate and stores:
        - TimeRemaining
        - TimeSpent
    """
    def __init__(self):
        self.time_remaining = 0
        self.time_spent = 0

    def calcTimeRemaining(self, User):
        """
        calculate remaining days. Returns in days unit
        """
        DoD = User.DoD
        today = date.today()
        d0 = date(DoD['year'], DoD['month'], DoD['day'])
        delta = today - d0
        return delta.days
    
    def calcTimeSpent(self, User):
        """
        calculate days spent and returns in days unit
        """
        DoB = User.DoB
        today = date.today()
        d0 = date(DoB['year'], DoB['month'], DoB['day'])
        delta = d0 - today
        return delta.days


