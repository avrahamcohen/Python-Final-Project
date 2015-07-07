#!/usr/bin/python

# Full Name: Avraham Cohen ID:038025797
# Final Project: Udacity Programming Foundations with Python
# Main Program

import sys
import array
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Excel Sheet Reader Class
from excelHandler import ClassExcel

#Class represent an a Excel Sheet
from scoresExcelSheet import ClassScore
from studyExcelSheet import ClassStudy
from repsExcelSheet import ClassReps

#Array Structure: [[Date], [Element], [Element], [Element], ... ]
values = []
colors = []
elements = []
y_limit = 0
y_label = ''
x_label = ''
is_date_sheet = True

def main_window_setup():
	plt.gcf().canvas.set_window_title('Excel Sheet Analyze Tool')
	mng = plt.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())
	if (is_date_sheet == True):
		plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
		plt.gca().xaxis.set_major_locator(mdates.DayLocator())
		plt.gcf().autofmt_xdate()
	plt.show()

# Convert array of dates
def get_date_axis(array):
	dates = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in array] 
	return dates

# Pulling elements into array of arrays
# Here you need to setup your prefrences !!!
def get_elements(file_name):
	global elements
	global values
	global colors
	global y_limit
	global y_label
	global is_date_sheet

	excel_handler = ClassExcel(file_name)

	########################################################
	#                                                      #
	#		Excel Sheet Name: scores.xlsx	       #
	#                                                      #
	########################################################

	if (file_name == 'scores.xlsx'):
		excel_handler.read_excel_sheet(ClassScore)

		elements = ClassScore.get_element_names()
		values = ClassScore.get_value_structure()
		colors = ClassScore.get_colors()
		
		values[0] = ClassScore.get_item('date', excel_handler.get_items())
		values[1] = ClassScore.get_item('snatch', excel_handler.get_items())
		values[2] = ClassScore.get_item('clean', excel_handler.get_items())
		values[3] = ClassScore.get_item('jerk', excel_handler.get_items())
		values[4] = ClassScore.get_item('dead_lift', excel_handler.get_items())
		values[5] = ClassScore.get_item('back_squat', excel_handler.get_items())
		values[6] = ClassScore.get_item('front_squat', excel_handler.get_items())
		values[7] = ClassScore.get_item('over_head_squat', excel_handler.get_items())
		values[8] = ClassScore.get_item('bench_press', excel_handler.get_items())

		y_limit = 200
		y_label = 'Weight (kg)'
		is_date_sheet = True

	########################################################
	#                                                      #
	#		Excel Sheet Name: study.xlsx	       #
	#                                                      #
	########################################################

	if (file_name == 'study.xlsx'):
		excel_handler.read_excel_sheet(ClassStudy)

		elements = ClassStudy.get_element_names()
		values = ClassStudy.get_value_structure()
		colors = ClassStudy.get_colors()
		
		values[0] = ClassStudy.get_item('date', excel_handler.get_items())
		values[1] = ClassStudy.get_item('math', excel_handler.get_items())
		values[2] = ClassStudy.get_item('english', excel_handler.get_items())
		values[3] = ClassStudy.get_item('spanish', excel_handler.get_items())

		y_limit = 100
		y_label = 'Grade'

		is_date_sheet = True

	########################################################
	#                                                      #
	#		Excel Sheet Name: reps.xlsx            #
	#                                                      #
	########################################################

	if (file_name == 'reps.xlsx'):
		excel_handler.read_excel_sheet(ClassReps)

		elements = ClassReps.get_element_names()
		values = ClassReps.get_value_structure()
		colors = ClassReps.get_colors()
		
		values[0] = ClassReps.get_item('sets', excel_handler.get_items())
		values[1] = ClassReps.get_item('pull_ups', excel_handler.get_items())
		values[2] = ClassReps.get_item('push_ups', excel_handler.get_items())
		values[3] = ClassReps.get_item('sit_ups', excel_handler.get_items())

		y_limit = 100
		y_label = 'Sets'

		is_date_sheet = False

		
def subsplot_setup(files):
	pos = 0

	if (len(files) == 1):

		f, axarr = plt.subplots(1)
		for file_name in files:
			get_elements(file_name)	
			axarr.set_title('For Excel Sheet: ' + file_name + '\n')
			axarr.set_ylabel(y_label)
			axarr.set_ylim([0,y_limit])

			space = 1
			data = 0

			for index in range(0,len(elements)):
				if (is_date_sheet == True):
					axarr.plot(get_date_axis(values[0]),values[data+1], color=colors[data])	
				else:
					axarr.plot(values[0],values[data+1], color=colors[data])
				axarr.text(1.005, space, elements[data], color=colors[data], horizontalalignment='left', verticalalignment='top', transform = axarr.transAxes)
				space = space - 0.10
				data = data + 1

			pos = pos + 1

	else:

		f, axarr = plt.subplots(len(files), sharex=False)
		for file_name in files:
			get_elements(file_name)	
			axarr[pos].set_ylabel(y_label)
			axarr[pos].set_ylim([0,y_limit])
			axarr[pos].grid(True)

			space = 1
			data = 0

			for index in range(0,len(elements)):
				if (is_date_sheet == True):
					axarr[pos].plot(get_date_axis(values[0]),values[data+1], color=colors[data])	
				else:
					axarr[pos].plot(values[0],values[data+1], color=colors[data])
				axarr[pos].text(1.005, space, elements[data], color=colors[data], horizontalalignment='left', verticalalignment='top', transform = axarr[pos].transAxes)
				space = space - 0.10
				data = data + 1

			pos = pos + 1

# Main Flow
values = []
for item in sys.argv:
	if (item != sys.argv[0]):
		values = values + [item]
subsplot_setup(values)
main_window_setup()
