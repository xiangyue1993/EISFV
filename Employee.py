class Employee:
    def __init__(self, number, averageSalary):
        self.number = number
        self.averageSalary = averageSalary

    def Employee_Wages_Cost(self):
        return self.number * self.averageSalary