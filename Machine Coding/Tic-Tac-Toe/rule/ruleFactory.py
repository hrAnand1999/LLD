from rule.colRule import ColRule
from rule.rowRule import RowRule
from rule.diagRule import DiagRule
from rule.Irule import IRule

class RuleFactory:

    def __init__(self):
        pass

    def createRule(self, type: str) -> IRule:
        if type == "col":
            return ColRule()
        elif type == "row":
            return RowRule()
        elif type == "diag":
            return DiagRule()
        else:
            print("Undefined type of rule")
            raise ValueError 