import json
from Pipe import Pipe
from PipeMaterial import PipeMaterial
from PipeOuterLayer import PipeOuterLayer
from HeatSource import HeatSource
from HeatLoad import HeatLoad
from Network import Network
from SalesInfo import SalesInfo
from LoanInfo import LoanInfo
from ManagementInfo import ManagementInfo
from Employee import Employee
from TaxInfo import TaxInfo
from ProjectInfo import ProjectInfo
from FinancialEvaluator import FinancialEvaluator

if __name__ == '__main__':
    fileObject = open("input.json")
    fileText = json.loads(fileObject.read())
    fileObject.close()

    pipeList = []
    sourceList = []
    loadList = []
    valveList = []
    pumpList = []
    for key, value in fileText["NetworkInfo"].items():
        if value["class_name"] == "Pipe":
            pipeMaterial = PipeMaterial(
                value["pipe_material"]["density"], value["pipe_material"]["unit_price"])
            pipeInsulationLayer = PipeOuterLayer(value["pipe_insulation_layer"]["thickness"],
                                                 value["pipe_insulation_layer"]["unit_price"])
            pipeAntiCorrosionLayer = PipeOuterLayer(value["pipe_anticorrosion_layer"]["thickness"],
                                                    value["pipe_anticorrosion_layer"]["unit_price"])
            pipeList.append(Pipe(value["pipe_id"], key, value["length"], value["inter_diameter"], value["wall_thickness"],
                                 pipeMaterial, pipeInsulationLayer, pipeAntiCorrosionLayer, value["pipe_unit_construction_price"]))
        elif value["class_name"] == "Source":
            sourceList.append(HeatSource(value["source_id"], key, value["mass_flow_rate"],
                                         value["energy_supply"], value["energy_source_type"], value["heating_device_price"],
                                         value["heating_device_installation_price"], value["heating_period_per_year"]))
        elif value["class_name"] == "Load":
            loadList.append(
                HeatLoad(value["load_id"], key, value["heating_area"]))
    heatNetwork = Network(pipeList, loadList, sourceList, valveList, pumpList)

    salesInfo = SalesInfo(
        heatNetwork, fileText["SalesInfo"]["heating_unit_price"])

    loanInfo = LoanInfo(fileText["LoanInfo"]["loan_raise_rate"], fileText["LoanInfo"]["lending_rate"],
                        fileText["LoanInfo"]["loan_period"], fileText["LoanInfo"]["interest_compounded_number"])

    employee = Employee(fileText["ManagementInfo"]["employees"]["number"],
                        fileText["ManagementInfo"]["employees"]["average_salary"])
    managementInfo = ManagementInfo(heatNetwork, fileText["ManagementInfo"]["energy_source_unit_price"],
                                    fileText["ManagementInfo"]["water_unit_price"], employee, fileText["ManagementInfo"]["water_replenish_rate"],
                                    fileText["ManagementInfo"]["device_depreciation_rate"], fileText["ManagementInfo"]["device_upkeep_rate"],
                                    fileText["ManagementInfo"]["other_expense_rate"], fileText["ManagementInfo"]["liquidity_rate"])

    taxInfo = TaxInfo(fileText["SalesInfo"]["TaxInfo"]["income_tax_rate"],
                      fileText["SalesInfo"]["TaxInfo"]["value_added_tax_rate"],
                      fileText["SalesInfo"]["TaxInfo"]["urban_maintenance_construction_tax_rate"],
                      fileText["SalesInfo"]["TaxInfo"]["education_supplementary_tax_rate"])

    projectInfo = ProjectInfo(fileText["ProjectInfo"]["project_life_cycle"],
                              fileText["ProjectInfo"]["project_construction_cycle"])

    financialEvaluator = FinancialEvaluator(
        projectInfo, heatNetwork, managementInfo, salesInfo, loanInfo, taxInfo)
    financialEvaluator.Financial_Evaluate()
