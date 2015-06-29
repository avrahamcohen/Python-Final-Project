#!/usr/bin/python

# Full Name: Avraham Cohen ID:038025797
# Final Project: Udacity Programming Foundations with Python
# Handler Program

import xlrd
from datetime import datetime, date, time
from xlrd import open_workbook, cellname, xldate_as_tuple

# This class handle the reading from the Excel sheet.
class excel_class:
  def __init__(self, fileName):
    self.fileName = fileName
    self.items = []

  def convertToDate(self, value):
    date_value = xldate_as_tuple(value, 0)
    return datetime(*date_value).strftime("%d/%m/%Y")

  def readExcelSheet(self, class_name):
    wb = open_workbook(self.fileName)
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols

        rows = []
        for row in range(1, number_of_rows):
            values = []
            for col in range(number_of_columns):
                if sheet.cell(row,col).ctype == xlrd.XL_CELL_DATE:
                  value = self.convertToDate((sheet.cell(row,col).value));
                else:
                  value = (sheet.cell(row,col).value)
                try:
                    value = str(int(value))
                except ValueError:
                    pass
                finally:
                    values.append(value)
            item = class_name(*values)
            self.items.append(item)

  def getItems(self):
    return self.items

