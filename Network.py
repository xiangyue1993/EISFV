from Pipe import Pipe
from PipeMaterial import PipeMaterial
from PipeOuterLayer import PipeOuterLayer
from HeatSource import HeatSource
from HeatLoad import HeatLoad

class Network:
    def __init__(self, pipeList, loadList, sourceList, valveList, pumpList):
        self.pipeList = pipeList
        self.loadList = loadList
        self.sourceList = sourceList
        self.valveList = valveList
        self.pumpList = pumpList

    def Devices_Purchasing_Cost(self):
        pipeTotalPurchasingCost = 0
        for item in self.pipeList:
            pipeTotalPurchasingCost = pipeTotalPurchasingCost + item.Pipe_Purchasing_Cost()

        sourceTotalPurchasingCost = 0
        for item in self.sourceList:
            sourceTotalPurchasingCost = sourceTotalPurchasingCost + item.Source_Purchasing_Cost()
        
        return pipeTotalPurchasingCost + sourceTotalPurchasingCost

    def Devices_Installation_Cost(self):
        pipeTotalInstallationCost = 0
        for item in self.pipeList:
            pipeTotalInstallationCost = pipeTotalInstallationCost + item.Pipe_Construction_Cost()

        sourceTotalInstallationCost = 0
        for item in self.sourceList:
            sourceTotalInstallationCost = sourceTotalInstallationCost + item.Source_Installation_Cost()

        return pipeTotalInstallationCost + sourceTotalInstallationCost