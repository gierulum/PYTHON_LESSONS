class func_class:

	def __init__(self, imie, nazwisko, wiek):
		self.imie = imie
		self.nazwisko = nazwisko
		self.wiek = wiek
	
	def text(self, imie, nazwisko):
		self.imie = imie
		self.nazwisko = nazwisko
		print ("Tutaj jest tekst z imieniem i nazwiskiem: %s %s" % (self.imie, self.nazwisko))
		
	def imie(self):
		print ("Moje imie to %s" % (self.imie))

			
	def obliczenia(self, obl_1=10):
		obl_sum = obl_1 + obl_1 
		print ("Wynikiem obliczen jest: %s " % (obl_sum))
		