import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scraper import get_count
import csv

def make_graph():

	cnt = get_count()[0]
	data = pd.read_csv('dates.csv')
	cases_number = data.iloc[:,0].values
	days = []

	for i in range(1, len(cases_number) + 1):
	    days.append(i)

	#updating data
	with open('dates.csv','a') as f:
	    writer=csv.writer(f)
	    writer.writerow([cnt])

	#making plot
	plt.plot(days, cases_number, color='b')
	#plt.figure(figsize=(2, 2))
	plt.xlabel('Days since March 02, 2020')
	plt.ylabel('Number of Cases')
	plt.title('COVID-19 Cases In India')
	plt.savefig('static/covid_plot.png')
	plt.show()

make_graph()