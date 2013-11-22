import arcpy
import pythonaddins

suburbList = []
suburbLayer = arcpy.SearchCursor("E:/AustraliaProject/data/parks.shp")                                  
for row in suburbLayer:
    suburbList.append(row.reg_park)
suburbSet = set(suburbList)
suburbuniqueList = list(suburbSet)

class SuburbBoxClass1(object):
    """Implementation for suburb.combobox (ComboBox)"""
    def __init__(self):
        self.items = sorted(suburbuniqueList)
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
        pass
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):               
        pass       
    def onEnter(self):
        pass
    def refresh(self):
        pass
