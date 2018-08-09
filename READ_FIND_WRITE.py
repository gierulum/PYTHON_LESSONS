import re
import sys
import os

'''
They are in RE module
Identifiers:
\d any number
\D anything but number
\s space
\S anything but a space
\w any character
\W anythong but a character
.  any character, except for a new line
b\ white space around words
\. period

Modifiers (amount of types or models of data):
{1, 3} we're excepting 1 - 3  (example: \d{1,3})
+ 		match 1 or more 
?		match 0 or 1
* 		match 0 or more
$ 		match the end of a string
^ 		match the beginning of a string
| 		either or  (example: d{1 - 3} | \w {5-6})
[]		range of values [A-Z][a-z]   (emample [A-Za-z1-5]) 
{x}		expecting "x" amount

White space characters: 
\n new line
\s space		
\t tab
\e escape
\f form feed
\r return

DONT FORGET!!:
. + * ? [] $ () ^ | \ 
'''

string = '''
Albert is 16, Admund has 23, Oscar could be like 70 and here was Amanda - she was 101 last summer.
'''

test_string = ''' 
ABCtest ROK 2016, wiek 30, SpRaWdZAMY jak TO dziala!?#$%%^&*
'''

hstring = '''
Albert is 16 and doc number A7ExD4, Admund has 23 (doc: 875Sde), Oscar could be like 70 (qQES48). There was Amanda (QES1271) - she was 101 last summer. That's a status in 2016.  
'''
#POCWICZYC!!!!!!
#LICZBY - liczba znakow mieszczaca sie miedzy 1 a 3
spr = re.findall(r'\d{1,3}',  test_string)
print (spr)
#ROK:
spr = re.findall(r'\d{4}',  test_string)
print (spr)

spr = re.findall(r'\D{1,3}',  test_string)
print (spr)
spr = re.findall(r'\s{1,3}',  test_string)
print (spr)
spr = re.findall(r'\S{1,3}',  test_string)
print (spr)
spr = re.findall(r'\w{1,3}',  test_string)
print (spr)
spr = re.findall(r'\W{1,3}',  test_string)
print (spr)




#regular expresion corespond to name and names:
#szukamy wieku ludzi - czyli liczba od 1 do 3 znaków - zarówno osoby z wiekiem 7 jak i tej z 101.
ages = re.findall(r'\d{1,3}', string)
names = re.findall(r'[A-Z][a-z]*', string)

print (ages)
print (names)

Dict = {} 
x = 0

for eachName in names:
	Dict[eachName] = ages[x]
	x+=1

print (Dict)
