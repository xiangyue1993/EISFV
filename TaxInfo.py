#coding:utf-8

class TaxInfo:
    def __init__(self, incomeTaxRate, valueAddedTaxRate,
                 urbanMaintenanceConstructionTaxRate, educationSupplementaryTaxRate):
        self.incomeTaxRate = incomeTaxRate
        self.valueAddedTaxRate = valueAddedTaxRate
        self.urbanMaintenanceConstructionTaxRate = urbanMaintenanceConstructionTaxRate
        self.educationSupplementaryTaxRate = educationSupplementaryTaxRate

    #增值税额=销项税额-进项税额
    def Value_Added_Tax(self, salesIncome, inputTax):
        # 销项税额=（含税）销售额/（1+税率）×税率
        outputTax = salesIncome / \
            (1 + self.valueAddedTaxRate) * self.valueAddedTaxRate
        return outputTax - inputTax

    def Urban_Maintenance_Construction_Tax(self, salesIncome, inputTax):
        return self.Value_Added_Tax(salesIncome, inputTax) * self.urbanMaintenanceConstructionTaxRate

    def Education_Supplementary_Tax(self, salesIncome, inputTax):
        return self.Value_Added_Tax(salesIncome, inputTax) * self.educationSupplementaryTaxRate

    #应纳税所得额=收入总额-不征税收入-免税收入-各项扣除-以前年度亏损
    def Income_Tax(self, salesIncome, inputTax, validManagementCost):
        return (salesIncome - self.Value_Added_Tax(salesIncome, inputTax) -
                self.Urban_Maintenance_Construction_Tax(salesIncome, inputTax) -
                self.Education_Supplementary_Tax(salesIncome, inputTax) - validManagementCost) * self.incomeTaxRate
