import epicthing
import statistics
from statistics import variance
import statistics as s
import csv
from statistics import variance as ss, mean as pp


#Reading from a CSV spreadsheet
import csv

#pobranie funkcji poprzez import z innego pliku z funkcja
epicthing.epic()

example_list = [1,3,4,6,8,9,102,15,36,1,89]

x = statistics.stdev(example_list)
y = s.stdev(example_list)
z = variance(example_list)
w = pp(example_list)
print(x)
print(y)
print(z)
print(w)

#listy 
multi = [[6,8], [1,32],[97,2]]

#wybiera wartosci listy lista_x[[numer_listy][pozycja_listy]]
# jezeli multi = [[6,8], [1,32],[97,2]] wtedy (multi[1][1]) = 32 (pozycje i listy zaczynaja sie nie od 1 ale od 0)  )
print (multi[1][1],[1])

#data from file example_csv
with open('example_csv.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ',')
	
	dates = []
	colors = []
	
	for row in readCSV:
		print (row)
		print (row[0])
		print (row[0], row[1])
		color = row[3]
		date = row[0]
		
		dates.append(date)
		colors.append(color)
	
	print(dates)
	print(colors)
	
	try:
		whatColor = input('What color do u wish to know?')
				
		if whatColor in colors:
			coldex = colors.index(whatColor.lower())
			theDate = dates[coldex]
			print('The date of ', whatColor, 'is: ', theDate)
		else:
			print ('Color not found')
	
	
	except Exception as e:
		print (e)
		
	print ('contuing')
	

dictionaries = {'JACK': 15 , 'BOB': 17}
print (dictionaries)
print (dictionaries['JACK'])
del dictionaries['JACK']

dict2 = {'ABC': [1,2], 'QWE': [1,8,6], 'POI': [89,45]}
print (dict2)
print(dict2['ABC'][1])
print(dict2['QWE'][2])
