import PipeOuterLayer

PI = 3.14159

class Pipe:
    def __init__(self, pipeID, pipeName, pipeLength, pipeInterDiameter, pipeThickness, \
    pipeMaterial, pipeInsulationLayer, pipeAnticorrosionLayer, pipeUnitConstructionPrice):
        self.pipeID = pipeID
        self.pipeName = pipeName
        self.pipeLength = pipeLength
        self.pipeInterDiameter = pipeInterDiameter
        self.pipeThickness = pipeThickness
        self.pipeMaterial = pipeMaterial
        self.pipeInsulationLayer = pipeInsulationLayer
        self.pipeAnticorrosionLayer = pipeAnticorrosionLayer
        self.pipeUnitConstructionPrice = pipeUnitConstructionPrice
        self.pipeOuterDiameter = pipeInterDiameter + pipeThickness * 2 + \
        pipeAnticorrosionLayer.thickness * 2 + pipeInsulationLayer.thickness * 2
        self.steelTotalWeight = PI * pipeInterDiameter * pipeThickness * pipeLength * pipeMaterial.density / 1000

    def Pipe_Purchasing_Cost(self):
        return self.steelTotalWeight * self.pipeMaterial.unitPrice + \
        self.pipeLength * self.pipeInsulationLayer.unitPrice + \
        self.pipeLength * self.pipeAnticorrosionLayer.unitPrice

    def Pipe_Construction_Cost(self):
        return self.pipeLength * self.pipeUnitConstructionPrice

    