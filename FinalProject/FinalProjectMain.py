#!/usr/bin/python

# Full Name: Avraham Cohen ID:038025797
# Final Project: Udacity Programming Foundations with Python
# Main Program

import sys
import array
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from FinalProjectHandler import excel_class
from scores import score_class
from study import study_class

#Array Structure: [[Date], [Element], [Element], [Element], ... ]
values = []
colors = []
elements = []
y_limit = 0
y_label = ''

def mainWindowSetup():
	plt.gcf().canvas.set_window_title('Excel Sheet Analyze Tool')
	mng = plt.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator())
	plt.gcf().autofmt_xdate()
	plt.grid(True)
	plt.show()

# Convert array of dates
def getDateAxis(array):
	dates = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in array] 
	return dates

# Pulling elements into array of arrays
# Here you need to setup your prefrences !!!
def getElements(file_name):
	global elements
	global values
	global colors
	global y_limit
	global y_label

	excel_handler = excel_class(file_name)

	########################################################
	#                                                      #
	#		Excel Sheet Name: scores.xlsx				   #
	#                                                      #
	########################################################

	if (file_name == 'scores.xlsx'):
		excel_handler.readExcelSheet(score_class)

		elements = score_class.getElementNames()
		values = score_class.getValueStructure()
		colors = score_class.getColors()
		
		values[0] = score_class.getItem('date', excel_handler.getItems())
		values[1] = score_class.getItem('snatch', excel_handler.getItems())
		values[2] = score_class.getItem('clean', excel_handler.getItems())
		values[3] = score_class.getItem('jerk', excel_handler.getItems())
		values[4] = score_class.getItem('dead_lift', excel_handler.getItems())
		values[5] = score_class.getItem('back_squat', excel_handler.getItems())
		values[6] = score_class.getItem('front_squat', excel_handler.getItems())
		values[7] = score_class.getItem('over_head_squat', excel_handler.getItems())
		values[8] = score_class.getItem('bench_press', excel_handler.getItems())

		y_limit = 200
		y_label = 'Weight (kg)'

	########################################################
	#                                                      #
	#		Excel Sheet Name: study.xlsx				   #
	#                                                      #
	########################################################

	if (file_name == 'study.xlsx'):
		excel_handler.readExcelSheet(study_class)

		elements = study_class.getElementNames()
		values = study_class.getValueStructure()
		colors = study_class.getColors()
		
		values[0] = study_class.getItem('date', excel_handler.getItems())
		values[1] = study_class.getItem('math', excel_handler.getItems())
		values[2] = study_class.getItem('english', excel_handler.getItems())
		values[3] = study_class.getItem('spanish', excel_handler.getItems())

		y_limit = 100
		y_label = 'Grade'
		
def subsplotSetup(files):
	pos = 0

	if (len(files) == 1):

		f, axarr = plt.subplots(1)
		for file_name in files:
			getElements(file_name)	
			axarr.set_title('For Excel Sheet: ' + file_name + '\n')
			axarr.set_ylabel(y_label)
			axarr.set_ylim([0,y_limit])

			space = 1
			data = 0

			for index in range(0,len(elements)):
				axarr.plot(getDateAxis(values[0]),values[data+1], color=colors[data])	
				axarr.text(1.005, space, elements[data], color=colors[data], horizontalalignment='left', verticalalignment='top', transform = axarr.transAxes)
				space = space - 0.10
				data = data + 1

			pos = pos + 1

	else:

		f, axarr = plt.subplots(len(files), sharex=False)
		for file_name in files:
			getElements(file_name)	
			axarr[pos].set_title('For Excel Sheet: ' + file_name + '\n')
			axarr[pos].set_ylabel(y_label)
			axarr[pos].set_ylim([0,y_limit])

			space = 1
			data = 0

			for index in range(0,len(elements)):
				axarr[pos].plot(getDateAxis(values[0]),values[data+1], color=colors[data])	
				axarr[pos].text(1.005, space, elements[data], color=colors[data], horizontalalignment='left', verticalalignment='top', transform = axarr[pos].transAxes)
				space = space - 0.10
				data = data + 1

			pos = pos + 1

# Main Flow
values = []
for item in sys.argv:
	if (item != sys.argv[0]):
		values = values + [item]
subsplotSetup(values)
mainWindowSetup()