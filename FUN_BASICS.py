##FUNCTION WITH ONE OR MORE ARGS:
def many_f_arg(arg1, *arg_next):
	print ("Output is: ")
	print (arg1)
	for x in arg_next:
		print (x)
	return;

many_f_arg(0,5)
many_f_arg(1,2,3,4,5)

##SIMPLE VARIABLES:
x,y = ('ABC', True)	
print (x)
print (y)	
	
##DECLARATION INPUT VARIABLE FOR NEXT FUNCTION:!	
string_here = input("Please insert values for function - check data type: ")
	
def  coop_string(string_here):
	if type(string_here) == float:
		print ('STRING HERE')
	elif type(string_here) == int:
		print ('INT HERE!')
	elif type(string_here) == str:
		print ('FLOAT HERE!!')
	

coop_string(string_here)

def while_function(args_wf):
	while float(args_wf) < 10 and float(args_wf) > 0:
		print (args_wf) 
		args_wf-=1

while_function(9)
	

abc = input("SET VALUE HERE: ")
def for_function(abc):
	print (abc)
	for cba in abc:
		print (cba + ' ' + abc)

for_function(abc)	

list_here = [1,2,3,48,94,10,5]
def list_function(list_here):
	for x in list_here:
		print (x)
	for x in range(1,5):
		print ('This is a range: ')
					
list_function(list_here)
		
def func_with_def(one, two = 7):
	one = 7
	summ = one * two
	print (summ)
	
func_with_def(1)	

def basic_window(width, height, font='TNR', bgc='W', scrollbar = True):
	print (width, height, font)

basic_window(250, 15, bgc='b')

global_val = 5
def function_glob_val(global_val):
	print (global_val)
	global_val = global_val + 10
	print (global_val)
	
function_glob_val(global_val)	
