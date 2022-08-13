from datetime import datetime

"""
User Class:
Holds User Information 
    - Date of Birth (DoB)
    - Date of Death (DoD)
Methods:
    - SetDoB()
    - SetDoD()
    - SetUnit()
"""

class User:
    """
    This class defines the users basic info
    """
    def __init__(self):
        self.DoB = None
        self.DoD = None
        self.Unit = None
    
    def setDoB(self, DoB):
        """
        DoB in the format of mm-dd-yyyy
        """
        # DoB = datetime.strptime(DoB, "%m/%d/%Y").strftime("%m-%d-%Y")
        month = int(DoB.split('-')[0])
        day = int(DoB.split('-')[1])
        year = int(DoB.split('-')[2])
        DoB = {"month":month, "day":day, "year":year}
        self.DoB = DoB
    
    def setDoD(self, DoD):
        """
        DoD in the format of mm-dd-yyyy
        """
        # DoD = datetime.strptime(DoD, "%m/%d/%Y").strftime("%m-%d-%Y")
        month = int(DoD.split('-')[0])
        day = int(DoD.split('-')[1])
        year = int(DoD.split('-')[2])
        DoD = {"month":month, "day":day, "year":year}
        self.DoD = DoD
    
    def setUnit(self, Unit="day"):
        """
        Unit: one of ["day", "week", "month", "year"]
        """
        self.Unit = Unit