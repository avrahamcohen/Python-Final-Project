#!/usr/bin/python

# Full Name: Avraham Cohen ID:038025797
# Final Project: Udacity Programming Foundations with Python
# Excel Sheet - study.xlsx

# This class represent one row from the Excel sheet
class study_class(object):
    def __init__(self, date, math, english, spanish):
        self.date = date
        self.math = math
        self.english = english
        self.spanish = spanish

    @staticmethod
    def getItem(item, items):
        values = []

        if (item == 'date'):
            for item in items:
                values = values + [format(item.date)]
            return values

        if (item == 'math'):
            for item in items:
                values = values + [format(item.math)]
            return values

        if (item == 'english'):
            for item in items:
                values = values + [format(item.english)]
            return values

        if (item == 'spanish'):
            for item in items:
                values = values + [format(item.spanish)]
            return values

    @staticmethod
    def getElementNames():
      return ['Math', 'English', 'Spanish']

    @staticmethod
    def getValueStructure():
    	return [[],[],[],[]]

    @staticmethod
    def getColors():
    	return ['blue','green','red','yellow']
