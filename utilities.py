import os, sys
#
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(base_path, relative_path)
#
class Year:
    def __init__(self,gross,_401k):
        # set gross pay for the year
        self.gross = gross
        # set baseline salary for the year
        self.salary = gross
        # set baseline net salary for the year
        self.net = 0
        # set starting 401k
        self._401k = _401k
    # calculate 401k gains for the year
    def calc_401k(self,percent):
        # calculate amount to add to 401k
        self._401k += self.gross * (percent/100)
        # calculate remaining salary
        self.salary = self.gross * (1-(percent/100))
    def calc_match(self,percent):
        # calculate amount to add to 401k
        self._401k += self.gross * (percent/100)
    # calculate taxes
    def taxes(self,rate):
        # calculate net salary based on tax percentage and remaining salary from 401k
        self.net = self.salary * (1-(percent/100))
    # calculate monthly income
    def monthly(self):
        # calculate monthly net based on net salary
        return self.net/12
    # calculate per paycheck income
    def paycheck(self):
        # calculate paycheck net based on net salary
        return self.net/26
#
def calc_raise(salary,percent,year):
    return salary*((1+percent)**year)
#
def calc_total_salary(salary,percent,years):
    final_salary = 0
    for i in range(1,years+1):
        final_salary += salary*((1+percent)**year)
    return final_salary