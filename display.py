import matplotlib.pyplot as plt
# import numpy as np
from datetime import datetime
from datetime import date

from pydantic import NoneStr

from user import User
from counter import Counter

"""
prepare data for display
generate data viz
"""

class Display:
    def __init__(self):
        self.width = None
        self.height = None
    
    def setWidth(self, width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height

    def convertDayToYearMonthDays(self, days):
        number_of_days = int(days)
        # Calculating years
        years = number_of_days // 365
        # Calculating months
        months = (number_of_days - years *365) // 30
        # Calculating days
        days = (number_of_days - years * 365 - months*30)

        return {"years":years, "months": months, "days":days}

    