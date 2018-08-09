import sys
from FUN_IMP import print_list
import CLASS_FUN


my_name = input("Whats u name?")
print ("My name is " + my_name)


my_list = [1,2,3,4,5,6]
for x in range(1,4):
	print(x)


def print_my_list(list_name):
	var_list_name = list_name
	for a in var_list_name:
		print (a)
		
print_list(my_list)	

osoba_one = CLASS_FUN.func_class("mariusz", "GGRZ", 34)

print (osoba_one.imie)
print (osoba_one.nazwisko)
print (osoba_one.wiek)

print("osoba jest dziedziczona... wiec ponizsze nie bedzie mialo nowych wartosci:")
osoba_one.text("Merkuriusz", "banal")

print("Mozemy to zmienic na :")
var_change_imie = input("Zmieniam imie na: ")
var_change_nazwisko = input("Zmieniam nazwisko na : ")
var_change_wiek = input("Zmieniam wiek na : ")


osoba_one = CLASS_FUN.func_class(var_change_imie, var_change_nazwisko, var_change_wiek)
print (osoba_one.imie)
print (osoba_one.nazwisko)
print (osoba_one.wiek)

print (CLASS_FUN.func_class.imie(osoba_one))

print ("Sprawdzamy obliczenia funkcji (wartosc domyslana jezeli puste!): ")
osoba_one.obliczenia()

