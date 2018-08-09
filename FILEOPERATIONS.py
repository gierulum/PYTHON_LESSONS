text = 'SAMPLE TEXT ABC\nNew line!'

def abc(a, b):
	sum = a + b
	print (sum)

abc(1,3)
	
#save data in file
saveFile = open('example.txt', 'w')
saveFile.write(text)
saveFile.close()

#append data to text file
AppendStrign = '\nAPPEND TEXT HERE!!'
appendFile = open('example.txt', 'a')
appendFile.write(AppendStrign)
appendFile.close()

#read file
readMe = open('example.txt', 'r').readlines()
print (readMe)