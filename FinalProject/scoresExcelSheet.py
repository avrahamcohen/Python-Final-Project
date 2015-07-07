#!/usr/bin/python

# Full Name: Avraham Cohen ID:038025797
# Final Project: Udacity Programming Foundations with Python
# Excel Sheet - scores.xlsx

# This class represent one row from the Excel sheet
class ClassScore(object):
    def __init__(self, date, snatch, clean, jerk, dead_lift, back_squat, front_squat, over_head_squat, bench_press):
        self.date = date
        self.snatch = snatch
        self.clean = clean
        self.jerk = jerk
        self.dead_lift = dead_lift
        self.back_squat = back_squat
        self.front_squat = front_squat
        self.over_head_squat = over_head_squat
        self.bench_press = bench_press

    @staticmethod
    def get_item(item, items):
	    values = []

	    if (item == 'date'):
	      for item in items:
	        values = values + [format(item.date)]
	      return values

	    if (item == 'snatch'):
	      for item in items:
	        values = values + [format(item.snatch)]
	      return values

	    if (item == 'clean'):
	      for item in items:
	        values = values + [format(item.clean)]
	      return values

	    if (item == 'jerk'):
	      for item in items:
	        values = values + [format(item.jerk)]
	      return values

	    if (item == 'dead_lift'):
	      for item in items:
	        values = values + [format(item.dead_lift)]
	      return values

	    if (item == 'back_squat'):
	      for item in items:
	        values = values + [format(item.back_squat)]
	      return values

	    if (item == 'front_squat'):
	      for item in items:
	        values = values + [format(item.front_squat)]
	      return values

	    if (item == 'over_head_squat'):
	      for item in items:
	        values = values + [format(item.over_head_squat)]
	      return values

	    if (item == 'bench_press'):
	      for item in items:
	        values = values + [format(item.bench_press)]
	      return values

    @staticmethod
    def get_element_names():
      return ['Snatch', 'Clean', 'Jerk', 'Dead Lift', 'Back Squat', 'Front Squat', 'Over Head Squat', 'Bench Press']

    @staticmethod
    def get_value_structure():
    	return [[],[],[],[],[],[],[],[],[]]

    @staticmethod
    def get_colors():
    	return ['blue','green','red','orange','magenta','yellow','black','gray']
