#my project:

Rooms = []
Films = []

class Cinema: 
    
    def __init__(self, name, room_num, rows_seats, col_seats):
        self._name = name
        self._room_num = room_num 
        self._rows_seats = rows_seats 
        self._col_seats = col_seats        
        
        self.seat_check_list = []
        #statuses: E - Empty, R - Resevation, B - buyed
        status = ["E", "R", "B"]
        a = int(self._rows_seats)
        b = int(self._col_seats)
        rows_in_room = "ABCDEFGHIJKLMNOPRSTUWZ"
        for x in range(a):
            a = rows_in_room[x:x+1]
            for y in range(b):
                seat_check = str(a) + str(y) + "E"
                self.seat_check_list.append(seat_check)
                
        new_room = {"id": self._name,
                    "room_num": self._room_num,
                    "rows_seats": self._rows_seats,
                    "col_seats": self.col_seats,
                    "seats_list": self.seat_check_list
                   }
        Rooms.append(new_room)
        
    
    def rows_seats(self):
        return self._rows_seats
    
    def col_seats(self):
        return self._col_seats

class Person:
    def __init__(self, name, surname, age, mail):
        self._name = name
        self._surname = surname
        self._age = age
        self._mail = mail
    
    def name(self):
        return self._name
    def surname(self):
        return self._surname
    def age(self):
        return self._age
    def mail(self):
        return self._mail
    
    
class Film:
    
    def __init__(self, film_name, type_film, time, age):
        self._film_name = film_name
        self._type_film = type_film
        self._time = time
        self._age = age

        fn = {"film_name": self._film_name, 
              "type_film": self._type_film,
              "time": self._time, 
              "age": self._age
         }
    
        Films.append(fn)
        
    def film_name(self):
        return self._film_name
    
    def type_film():
        return self._type_film
    
    def time(self):
        return self._time
    
    def age(self):
        return self._age
    

        
class Tickets:
    def __init__(self, cinema, film, room):
        self._room = room
        self._film = film
        self._room = room      

    def Check_Tickets(self):
        info = ""
        for i in Rooms:
            if self._room == i["room_num"]: 
                info = info + "room: true, "
            else:
                info = info + "room: false, "
            
        for x in Films:
            if self._film == x["film_name"]:
                info = info + "film: true"
            else:
                info = info + "film: false"
        
        list_of_seats = str(list(map(lambda x : x['seats_list'], Rooms)))
        return info +  list_of_seats    
        
    
    def Order_Ticket(self, room, person, seat):
        self._room = room
        self._person = person
        self._seat = seat
        
        for x in Rooms:
            for index, item in enumerate(x["seats_list"]):
                if item == self._seat + "E":
                    x["seats_list"][index] = self._seat+"B" 
                    #x["seats_list"][] = self._seat+"R"
                    return a
    
    
a = Cinema("Zlote Tarasy", 3, "12", "22")
p = Person("John", "Snow", 32, "aaa@gmail.com")
f = Film("Johny Wick", "action", 140, 16)

#print(Films[0])
#print(p.surname())
#print(f.time())
t = Tickets("Zlote Tarasy","Johny Wick", 3)
#t.Check_Tickets()
t.Order_Ticket(3, "PP", "A1")

t.Check_Tickets()
