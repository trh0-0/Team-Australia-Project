import arcpy
import pythonaddins

'''class Statistics_Button(object):
    # initialize the wizard_addin.button (Button)
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass'''
import arcpy
import pythonaddins
suburb_row = row.SED_Name   #Needs to be dynamic
suburbList = []
suburbLayer = arcpy.SearchCursor("E:/AustraliaProject/data/parks.shp")   #Needs to be dynamic                               
for row in suburbLayer:
    suburbList.append(suburb_row)
suburbSet = set(suburbList)
suburbuniqueList = list(suburbSet)

class SuburbComboBox(object):
    """Implementation for suburb.combobox (ComboBox)"""
    def __init__(self):
        self.items = sorted(suburbuniqueList)
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
        # When an item is selected, make it the only selectable area.
        layer = arcpy.mapping.ListLayers(self.mxd, selection)[0]
        desc = arcpy.Describe(layer.dataSource)
        extent = desc.Extent
        
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        # When the combo box has focus, update the combo box with the list of layer names.
        if focused:
            self.mxd = arcpy.mapping.MapDocument('current')
            layers = arcpy.mapping.ListLayers(self.mxd)
            self.items = []
            for layer in layers:
                self.items.append(layer.name)
        
    def onEnter(self):
        pass
    def refresh(self):
        pass
   
# Make the Public Open Space Combobox    	
pos_List = []
sel_row = row.reg_park                                                  #This need to be dynamic. getparametersastext?
pos_Layer = arcpy.SearchCursor("E:/AustraliaProject/data/parks.shp")    # Needs to be dynamic                                  
for row in pos_Layer:
    pos_List.append(sel_row)   
posSet = set(suburbList)
posuniqueList = list(posSet)

class POS_ComboBox(object):
    """Implementation for pos.combobox (ComboBox)"""
    def __init__(self):
        self.items = sorted(posuniqueList)
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
        pass
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):               
        # When the combo box has focus, update the combo box with the list of layer names.
        if focused:
            self.mxd = arcpy.mapping.MapDocument('current')
            layers = arcpy.mapping.ListLayers(self.mxd)
            self.items = []
            for layer in layers:
                self.items.append(layer.name)      
    def onEnter(self):
        pass
    def refresh(self):
        pass
 
