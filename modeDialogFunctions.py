from variables import *


def mdRadianFunction(ui):
    if ui.mdRadianButton.isChecked():
        ui.mdDegreeButton.setChecked(False)
        modeStates["degradState"] = "rad"


def mdDegreeFunction(ui):
    if ui.mdDegreeButton.isChecked():
        ui.mdRadianButton.setChecked(False)
        modeStates["degradState"] = "deg"