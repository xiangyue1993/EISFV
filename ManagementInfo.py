#coding:utf-8

from Network import Network
from Employee import Employee
from HeatSource import HeatSource

#每立方米天然气热值，单位：焦耳
unitGasCalorificValue = 35587375
#每度电对应热值，单位：焦耳
unitPowerCalorificValue = 3600000

class ManagementInfo:
    def __init__(self, heatNetwork, energySourceUnitPrice, waterUnitPrice, employees, \
    waterReplenishRate, deviceDepreciationRate, deviceUpkeepRate, otherExpenseRate, liquidityRate):
        self.heatNetwork = heatNetwork
        self.energySourceUnitPrice = energySourceUnitPrice
        self.waterUnitPrice = waterUnitPrice
        self.employees = employees
        self.waterReplenishRate = waterReplenishRate
        self.deviceDepreciationRate = deviceDepreciationRate
        self.deviceUpkeepRate = deviceUpkeepRate
        self.otherExpenseRate = otherExpenseRate
        self.liquidityRate = liquidityRate

    def Energy_Source_Cost(self):
        totalEnergySourceCost = 0
        for source in self.heatNetwork.sourceList:
            if source.energySourceType == "gas":
                totalEnergySourceCost += source.Total_Energy_Supply_Per_Year() / unitGasCalorificValue * self.energySourceUnitPrice
            elif source.energySourceType == "power":
                totalEnergySourceCost += source.Total_Energy_Supply_Per_Year() / unitPowerCalorificValue * self.energySourceUnitPrice
        return totalEnergySourceCost

    def Water_Cost(self):
        totalWaterCost = 0
        for source in self.heatNetwork.sourceList:
            totalWaterCost += source.massFlowRate * 3600 * 24 * source.heatingPeriodPerYear * \
            self.waterReplenishRate / 1000 * self.waterUnitPrice
        return totalWaterCost

    def Employee_Wages_Cost(self):
        return self.employees.Employee_Wages_Cost()

    def Device_Depreciation_Cost(self):
        return self.heatNetwork.Devices_Purchasing_Cost() * self.deviceDepreciationRate

    def Device_Upkeep_Cost(self):
        return self.heatNetwork.Devices_Purchasing_Cost() * self.deviceUpkeepRate

    def Other_Expense_Cost(self):
        return (self.heatNetwork.Devices_Purchasing_Cost() + self.heatNetwork.Devices_Installation_Cost()) * \
        self.otherExpenseRate
        
    def Liquidity_Amount(self):
        return (self.Energy_Source_Cost() + self.Water_Cost() + self.Employee_Wages_Cost() + \
        self.Device_Depreciation_Cost() + self.Device_Upkeep_Cost() + self.Other_Expense_Cost()) * self.liquidityRate


