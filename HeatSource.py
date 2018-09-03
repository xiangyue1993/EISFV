class HeatSource:
    def __init__(self, sourceID, sourceName, massFlowRate, energySupply, energySourceType, \
    heatingDevicePrice, heatingDeviceInstallationPrice, heatingPeriodPerYear):
        self.sourceID = sourceID
        self.sourceName = sourceName
        self.massFlowRate = massFlowRate
        self.energySupply = energySupply
        self.energySourceType = energySourceType
        self.heatingDevicePrice = heatingDevicePrice
        self.heatingDeviceInstallationPrice = heatingDeviceInstallationPrice
        self.heatingPeriodPerYear = heatingPeriodPerYear

    def Source_Purchasing_Cost(self):
        return self.heatingDevicePrice

    def Source_Installation_Cost(self):
        return self.heatingDeviceInstallationPrice

    def Total_Energy_Supply_Per_Year(self):
        return self.energySupply * 3600 * 24 * self.heatingPeriodPerYear