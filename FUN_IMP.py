import sys


my_name = input("Whats u name?")
print ("My name is " + my_name)


my_list = [1,2,3,4,5,6]
for x in range(1,4):
	print(x)


def print_list(list_name):
	var_list_name = list_name
	for a in var_list_name:
		print (a)
		
print_list(my_list)	
