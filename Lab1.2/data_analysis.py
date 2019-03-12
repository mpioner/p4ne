from matplotlib import pyplot
from openpyxl import load_workbook
import pprint

import os
#print (os.getcwd())
wb = load_workbook('.\\Lab1.2\\data_analysis_lab.xlsx')

sheet = wb['Data']
#sheet['A'][1:]
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(list(sheet))
def getvalue(x): return x.value

pyplot.plot(list(map(getvalue, sheet['A'][1:])), list(map(getvalue, sheet['B'][1:])), label="Metka")
pyplot.plot(list(map(getvalue, sheet['A'][1:])), list(map(getvalue, sheet['C'][1:])), label="Metka2")
pyplot.plot(list(map(getvalue, sheet['A'][1:])), list(map(getvalue, sheet['D'][1:])), label="Metka3")
pyplot.show()
