#import time
import math

#dostep do biblioteki time w tym wyswietlenie informacji o formatach
#help(time)

list_a = [1,2,9,12,91,7]

def max_value(arg = input('name u argument!')):
	print (arg)
	max_val = max(arg)
	print (max_val)
	
	
#print (max_value([lista wartosci]))
print (max_value(list_a))

list_b = [2,6,99,12,91,7]

def comp_list(arg_list_1 = input('lista pierwsza: '), arg_list_2 = input('lista druga: ')):
	print (arg_list_1)
	print (arg_list_2)
	for x in arg_list_1:
		print(x)
		for y in arg_list_2:
			print(y)
			if x > y:
				print ('x is greater or same')
			else:
				print ('y is greater')

print (comp_list(list_a, list_b))				
	
def conv_val(val = input('Please set value for conv: '), type = input('Please set data type of value: ')):
	val_const = val
	type_const = type
	print (val_const)
	print (type_const)
	
	print ("u cont type: %r" % type_const) 
	
	if type_const == 'str':
		func_val = str(val_const)
	elif type_const == 'int':
		func_val = int(val_const)
	elif type_const == 'float':
		func_val = float(val_const)
	else:
		func_val == str(val_const)
	print (func_val)
	
print (conv_val())
	