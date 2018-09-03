class SalesInfo:
    def __init__(self, Network, heatingUnitPrice):
        self.loadList = Network.loadList
        self.heatingUnitPrice = heatingUnitPrice

    def Sales_Income(self):
        totalSalesIncome = 0
        for load in self.loadList:
            totalSalesIncome += load.loadHeatingArea * self.heatingUnitPrice
        return totalSalesIncome