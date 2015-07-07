#!/usr/bin/python

# Full Name: Avraham Cohen ID:038025797
# Final Project: Udacity Programming Foundations with Python
# Excel Sheet - reps.xlsx

# This class represent one row from the Excel sheet
class ClassReps(object):
    def __init__(self, sets, pull_ups, push_ups, sit_ups):
        self.sets = sets
        self.pull_ups = pull_ups
        self.push_ups = push_ups
        self.sit_ups = sit_ups

    @staticmethod
    def get_item(item, items):
        values = []

        if (item == 'sets'):
            for item in items:
                values = values + [format(item.sets)]
            return values

        if (item == 'pull_ups'):
            for item in items:
                values = values + [format(item.pull_ups)]
            return values

        if (item == 'push_ups'):
            for item in items:
                values = values + [format(item.push_ups)]
            return values

        if (item == 'sit_ups'):
            for item in items:
                values = values + [format(item.sit_ups)]
            return values

    @staticmethod
    def get_element_names():
      return ['Pull Ups', 'Push Ups', 'Sit Ups']

    @staticmethod
    def get_value_structure():
    	return [[],[],[],[]]

    @staticmethod
    def get_colors():
    	return ['blue','green','red','yellow']
