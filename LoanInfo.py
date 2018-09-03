class LoanInfo:
    def __init__(self, loanRaiseRate, lendingRate, loanPeriod, interestCompoundedNumber):
        self.loanRaiseRate = loanRaiseRate
        self.loanPeriod = loanPeriod
        self.effectiveLendingRate = (1 + lendingRate / interestCompoundedNumber)**interestCompoundedNumber - 1
        
    def Loan_Payment(self, totalLoan, yearNumber):
        principalPayment = totalLoan / self.loanPeriod
        interestPayment = (totalLoan - (yearNumber - 1) * principalPayment) * self.effectiveLendingRate
        return principalPayment + interestPayment