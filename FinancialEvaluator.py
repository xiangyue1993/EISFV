#coding:utf-8

from Network import Network
from ManagementInfo import ManagementInfo
from LoanInfo import LoanInfo
from TaxInfo import TaxInfo
from ProjectInfo import ProjectInfo
from SalesInfo import SalesInfo

import matplotlib.pyplot as plt
from pylab import mpl

class FinancialEvaluator:
    def __init__(self, projectInfo, heatNetwork, managementInfo, salesInfo, loanInfo, taxInfo):
        self.projectInfo = projectInfo
        self.heatNetwork = heatNetwork
        self.managementInfo = managementInfo
        self.salesInfo = salesInfo
        self.loanInfo = loanInfo
        self.taxInfo = taxInfo

    def Financial_Evaluate(self):
        constructionCost = self.heatNetwork.Devices_Purchasing_Cost() + self.heatNetwork.Devices_Installation_Cost()
        liquidity = self.managementInfo.Liquidity_Amount()
        totalLoan = (constructionCost + liquidity) * self.loanInfo.loanRaiseRate
        managementCost = self.managementInfo.Energy_Source_Cost() + self.managementInfo.Water_Cost() + \
        self.managementInfo.Employee_Wages_Cost() + self.managementInfo.Device_Depreciation_Cost() + \
        self.managementInfo.Device_Upkeep_Cost() + self.managementInfo.Other_Expense_Cost()

        cumulativeNetCash = 0
        cumulativeNetCashList = []
        returnRate = 0.12
        cumulativNetPresentValue = 0
        cumulativNetPresentValueList = []
        yearList = []
        i = 0
        while i < self.projectInfo.projectConstructionCycle:
            netCash = 0
            netCash -= constructionCost / self.projectInfo.projectConstructionCycle
            if i == 0:
                netCash += totalLoan
            if i >= 1 and i <= self.loanInfo.loanPeriod:
                netCash -= self.loanInfo.Loan_Payment(totalLoan, i)

            cumulativeNetCash += netCash
            cumulativeNetCashList.append(cumulativeNetCash)

            i += 1
            cumulativNetPresentValue += netCash * (1 + returnRate)**(-i)
            cumulativNetPresentValueList.append(cumulativNetPresentValue)
            yearList.append(i)
            
        while i >= self.projectInfo.projectConstructionCycle and i < self.projectInfo.projectLifeCycle:
            netCash = 0
            if i == self.projectInfo.projectConstructionCycle:
                netCash -= liquidity

            if i >= 1 and i <= self.loanInfo.loanPeriod:
                netCash -= self.loanInfo.Loan_Payment(totalLoan, i)

            salesIncome = self.salesInfo.Sales_Income()
            netCash += salesIncome

            inputTax = (self.managementInfo.Energy_Source_Cost() + self.managementInfo.Water_Cost() + \
            self.managementInfo.Device_Upkeep_Cost()) * self.taxInfo.valueAddedTaxRate
            validManagementCost = managementCost - self.managementInfo.Device_Depreciation_Cost() - \
            self.managementInfo.Device_Upkeep_Cost()
            totalTax = self.taxInfo.Value_Added_Tax(salesIncome, inputTax) + \
            self.taxInfo.Urban_Maintenance_Construction_Tax(salesIncome, inputTax) + \
            self.taxInfo.Education_Supplementary_Tax(salesIncome, inputTax) + \
            self.taxInfo.Income_Tax(salesIncome, inputTax, validManagementCost)
            netCash -= totalTax

            cumulativeNetCash += netCash
            cumulativeNetCashList.append(cumulativeNetCash)

            i += 1
            cumulativNetPresentValue += netCash * (1 + returnRate)**(-i)
            cumulativNetPresentValueList.append(cumulativNetPresentValue)
            yearList.append(i)
        
        mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

        plt.bar(yearList, cumulativNetPresentValueList, color='blue')
        plt.xlabel(u"项目计算期")
        plt.ylabel(u"累积净现值")
        graphTitleName = u"项目周期内的财务净现值变化趋势（内部收益率 = " + str(returnRate * 100) + u"%)"
        plt.title(graphTitleName)
        plt.show()
