#!/usr/bin/python

# Full Name: Avraham Cohen ID:038025797
# Final Project: Udacity Programming Foundations with Python
# Excel Sheet - study.xlsx

# This class represent one row from the Excel sheet
class ClassStudy(object):
    def __init__(self, date, math, english, spanish):
        self.date = date
        self.math = math
        self.english = english
        self.spanish = spanish

    @staticmethod
    def get_item(item, items):
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
    def get_element_names():
      return ['Math', 'English', 'Spanish']

    @staticmethod
    def get_value_structure():
    	return [[],[],[],[]]

    @staticmethod
    def get_colors():
    	return ['blue','green','red','yellow']
