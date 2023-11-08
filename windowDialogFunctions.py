from variables import *


def XminFunction(ui):
    try:
        lowerXLimit[0] = int(ui.Xmin.text())
    except:
        pass


def XmaxFunction(ui):
    try:
        upperXLimit[0] = int(ui.Xmax.text())
    except:
        pass


def XscaleFunction(ui):
    try:
        xScale[0] = int(ui.Xscale.text())
    except:
        pass


def YminFunction(ui):
    try:
        lowerYLimit[0] = int(ui.Ymin.text())
    except:
        pass


def YmaxFunction(ui):
    try:
        upperYLimit[0] = int(ui.Ymax.text())
    except:
        pass


def YscaleFunction(ui):
    try:
        yScale[0] = int(ui.Yscale.text())
    except:
        pass

