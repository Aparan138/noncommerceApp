import openpyxl
from openpyxl.styles import PatternFill
def getRowCount(file,SheetName):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook[SheetName]
    return sheet.max_row

def getColumnCount(file,SheetName):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook[SheetName]
    return sheet.max_column

def readData(file,sheetName,rownum,columno):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook[sheetName]
    return sheet.cell(rownum,columno).value

def writeData(file,sheetName,rownum,columno,data):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook[sheetName]
    sheet.cell(rownum,columno).value = data
    workbook.save(file)

def fillGreenColor(file,sheetName,rownum,columno):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook[sheetName]
    greenFill= PatternFill(start_color='60b212',
                            end_color='60b212',
                           fill_type='solid')
    sheet.cell(rownum,columno).fill = greenFill
    workbook.save(file)

def fillRedColor(file,sheetName,rownum,columno):
    workbook=openpyxl.load_workbook(file)
    sheet=workbook[sheetName]
    redFill= PatternFill(start_color='ff0000',
                            end_color='ff0000',
                           fill_type='solid')
    sheet.cell(rownum,columno).fill = redFill
    workbook.save(file)
