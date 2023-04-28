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