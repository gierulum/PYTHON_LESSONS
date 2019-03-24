def add_units(a , b):
    return a + b

print (add_units(2,5))

c = 12.34656
um = 412443.1343

print(c)
print(float(c))
###print(int(c))

word = "helloa"
print(word.replace("a","e"))
print(word.capitalize())

print(word.isalpha())

"aqwe,qwqtqwr,qwewe".split(",")


"my name is {0} and i love {1}".format(word, c)

check = 1

if check == 2:
    print("true")
else:
    print("false")

#not if:
#if check != 2:
if not check == 2:
    print("true")

    
#LISTS:
list_test = ["john" , "Mila", "Arnold"]
list_test[1]
list_test.append("Josh")
print(list_test)

print("Josh" in list_test)
len(list_test)
del list_test[0]

print(list_test)

#LISTS:
for x in list_test:
#    print("u just printed {x} as a name") << not working!!
    print("u just printed {0} as a name".format(x))

ww = 0
#od 15 do 30 z inkrementacja co 2:
for y in range(15,30,2):
#for y in range(10):
    ww = ww+y

print(ww)

print("          ")
print("PIERWSZA LISTA!!!")

list_long = ["a", "b" , "c", "d", "e"]
for x in list_long:
    if x == "c":
        print("found him!")
        break
    else:
        print("not yet")
        
print("          ")
print("DRUGA LISTA!!!")
        
list_longs = ["a", "b" , "c", "d", "e"]
for x in list_longs:
    if x == "c":
        #dla continue spełnionego nie jest zwracana wartosc - skrypt warunku jest pomijany:
        continue
        print("found him!")
    else:
        print("not yet")

print("          ")        
print("WHILE LOOP")       
        
zz = 0
while zz < 10:
    print("tutaj jest zawartosc {0}".format(zz))
    zz += 1

    
print("          ")    
print("DICTIONARIES")

student ={
    "imie" : "Marek",
    "nazwisko": "Markowski",
    "wiek":24   
}

student["imie"]
student.get("kraj", "brak")
student.keys()
student.values()

try:
    student["obywatel"]
except KeyError:
    print("this is error of key student")
	
	
	
	###################################################################
	
	
	list_pracownikow = []

def new_firms(name, *args):
    print(name)
    print(args)
    
new_firms("aaaa","bbbb","cccc","dddd")    


def new_employee(name, surname, age, department):
    seq_num = len(list_pracownikow) + 1
    student = {
        "id": seq_num,
        "name": name,
        "surname": surname,
        "age": age,
        "department": department
    }
    list_pracownikow.append(student)
    
new_employee("marek", "bodnar", 11, "ukrainian")
#or: new_employee(name="marek", surname="bodnar", age=11, department="ukrainian")


name_employee = input("Please, enter student name: ")
surname_employee = input("Please, enter student surname: ")
age_employee = input("Please, enter student age: ")
department_employee = input("Please, enter student department: ")

new_employee(name_employee, surname_employee , age_employee, department_employee)

print(list_pracownikow)



####################################################



num = 0

def save_file(bb):
    try:
        #a - appending to a new or existing file
        #w - writing overwrites the entire file
        #r - reading a text file
        #rb - reading a binary file
        #wb - writing a binry file
        
        f = open("stundents.txt", "a")
        for x in range(10):
            num = num + x
            f.write(num + "\n")
            f.close()
        #except Exception:
        #    print("Could not save file!")
        
        
def r_file():
    f = open("stundents.txt", "r")
    for x in f.readlines():
        print(x)
    f.close()
    #except Exception:
    #    print("Could not read a file")



save_file()
#read_file()
            
            
			###################################################
			
			
			
			Employee = []


class Workers:
    
    seq = 0
    school_name = "qwqwrqrqr"
    
    def get_school_name(self):
        return self.school_name
    
    #def add_worker(self, name, surname, age):
    def __init__(self, name, surname="abcd", age=11):
        self.name = name
        self.surname = surname
        self.age = age
        worker = {"name": self.name.capitalize(), "surname": self.surname.capitalize(), "age": age , "worker_id": seq}
        Employee.append(worker)        
    
    def get_name_capitalize(self):
        return self.name.capitalize()
        
    def __str__(self):
        return "lalala"

class WorkersPlace(Workers):
    def get_name_capitalize(self):
        orginal_value = super().get_name_capitalize()
        return orginal_value + "-HS"
    
#if def add_worker(self, name, surname, age) then all below could work: 
    
#empl = Workers()
print(empl.get_school_name)
#empl.add_worker("Mark", "Markus", 43)
#empl.add_worker("Anna", "ABC", 21)


print(Employee)

#when add_worker "is __init__" few parameters are default
#with __init__ james below works with surname and age on default values from constructor:

james = WorkersPlace("james")
print(james.get_name_capitalize())


####################################


list_alfa = list("abcdefgh")

list_a = ["asqwe", "qwqewaaae", "qweqastwe234353"]
list_b = []
o = 0
r = 0
a = list(list_a)


for x in list_a:
    r_loop = len(list_a[o])
    for y in range(r_loop):
        list_b.append(list_a[o][r])
        r = r + 1
    o = o+1
    r = 0
print(list_alfa)
print(a)
print(list_b)



elements = {"colors": "123543", "function": "manager" , "name": "cristian"}
for e in elements:
    print(e, elements[e])

			
######################################
			

#tests:


def maxmin(elem):
    return min(elem), max(elem)

a = [32323,35,4654,65,0]
b = ["qweq", "eqweq", "weqwe3 453 fd"]

maxmin(a)


b = ';'.join(b)
print(b)
b.split(";")

str = "unforgetable"
print(str.partition("forget"))
print(str)

a, b, c, d = "arizona;wisconsin;LA;washington".split(";")
print(a, b , c, d)

elem = [1244,535,657, 35545,5344,656563,454,234]
"strin {elem[1]} string {elem[2]} string string {elem[0]}".format(elem=elem)

#range(start, stop, step)
for x in range(0,10,2):
    print(x)

print(elem[2:], elem[:1], elem[2:3])

a = [[1,2],[3,4]]
b = a[:]
print("a" , a)
print("b" , b)

a[0] = [8,9]
print("a" , a)
print("b" , b)

a[1].append(5)
print("a" , a)
print("b" , b)

del elem[2]
elem.remove(5344)
print(elem)
elem+=[3425,657,8787,878,235]
print(elem)
elem.extend([444656,5353])
print(elem)

elem.sort()
print(elem)

yy = sorted(elem)
ee = reversed(yy)
print(ee, "its reverse iterator")
print(list(ee), "this is a list of ee")


var_aae = dict(aaa = '1242', qweqwe='3er235')
for key in var_aae:
    print("{key} => {value}".format(key=key, value = var_aae[key]))

for value in var_aae.values():
    print(value)
    
for key in var_aae.values():
    print(key)

for key, value in var_aae.items():
    print(key, value)
    
	
	###################################
	

#Iterables:
#list comprehensions:

words = "string my string again, some new words, expresions, some default etc".split()
# not work like words.split()

[len(word) for word in words]
lengths = []
for word in words: 
    lengths.append(len(word))
print(lengths)

#from math import factorial
#f = [len(str(factorial(x))) for x in range(20)]


from pprint import pprint as pp

country_to_capital = {'United Kingdom': 'London',
                     'Brazil': 'Brazilia',
                     'Marocc':'Rabat',
                     'Sweden':'Stockholm'}
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)

#end comprehension!!


from math import sqrt 

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i ==0:
            return False
    return True

[x for x in range(101) if is_prime(x)]


###########################################


#Iterators:

iterable = ['spring', 'summer','autumn', 'winter']
iterator = iter(iterable)
next(iterator)
next(iterator)
next(iterator)

def next_iteration(i, n):
    list_i = i
    iterator = iter(list_i)
    try:
        for x in range(n):
            e = next(iterator)
        return e
    except StopIteration:
        raise ValueError("iterable is empty")
    except ValueError:
        raise ValueError("iterable is empty")
        
i_e = ['spring', 'summer','autumn', 'winter']
print(next_iteration(i_e,3))


######################################


#classes:

#self is similar to "this" in C# or java
#__init__ is initializer - not a constructor
#avoid name clash

#endure, truths

class Flight_fly:
    def __init__(self, num, aircraft):
        if num == None:
            return "more than 0"
        
        
        self._num = num   
        self._aircraft = aircraft
    
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows  ]
    
    def num(self):
        return self._num
    
    def airline(self):
        return self._airline
        
    def allocate_seat(self, seat, passanger):
        rows, seat_leters = self.aircraft.seating_plan()
        
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
    
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat letter {}".format(row_text))
        
        self._seating[row][letter] = passenger
        
class Aircraft: 
    def __init__ (self, registration, model, num_rows , num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        
    def registration(self):
        return self._registration
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1, self._num_rows +1),
               "ABCDEFGHJK"[:self._num_seats_per_row])
    
f = Flight_fly("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows = 22, num_seats_per_row=6))    
f._seating
f.allocate_seat('12A', 'joanna joananna')
f._seating


###############################################



#see more open() modes!!

f = open('wasteland.txt', mode='wt', encoding='utf-8')
f.write('where is thats? \n our version is here correct\n and its very interesting text \n for reading using python')
f.close()

#appending
h = open('wasteland.txt', mode='at', encoding='utf-8')
h.writelines([' aaaaa aaww \n,', ' qweqda qw q qw q efwe \n ', ' dqwq  bfu wbeuw in ' ])
h.close()

g = open('wasteland.txt', mode='rt', encoding='utf-8')
#g.read(12)
print("--------")
#g.seek(0)
print("--------")
g.readline()
print("----next readline because of iteration:----")
g.readline()
print("--------")
g.close
#g.read()

"""
import sys

def main(filename):
    f = open(filename, mode = 'rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line
    f.close()
                         
if __name__ == '__main__':
    main(sys.argv[1])
"""


######



import urllib
import urllib.request
type(urllib)
type(urllib.request)
urllib.__path__




    