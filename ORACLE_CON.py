import cx_Oracle
import time

con = cx_Oracle.connect('sys/Leopold666@localhost:1521/orcl', mode=cx_Oracle.SYSDBA)

#'localhost:1521/orcl;DBA PRIVILEGE=SYSDBA;PERSIST SECURITY INFO=True;USE')
start  = time.time()
ver = con.version.split(".")
print (ver)
cur = con.cursor()
cur.execute('select * from AA_ABSENCJE')
row = cur.fetchone()

print ('Normal result print')
for result in cur:
	elapsed = (time.time() - start)
	print (result)
	print (elapsed)
	
print ('row fatchone')	
for result in cur:	
	elapsed_a = (time.time() - start)
	print (row)
	print (elapsed_a)
	
#print ver.index("1")
#ver.remove("2")

print ('Data insert: ')
cur.execute('insert into aa_absencje(data_od, data_do, prac_id, abs_id) values (sysdate, sysdate, 2, 2)')
con.commit()
print ('Data inserted!')

print ('Select inserted items: ')
cur2 = con.cursor()
cur.execute('select * from AA_ABSENCJE where abs_id = 2')
	
rows = [ (1, "First" ),
         (2, "Second" ),
         (3, "Third" ),
         (4, "Fourth" ),
         (5, "Fifth" ),
         (6, "Sixth" ),
         (7, "Seventh" ) ]	
	
for x in rows:
	cur.executemany("insert into aa_mypyth (id, data) values (:1, :2)", rows)
	con.commit()
	
	
cur3 = con.cursor()
lines = [55, 23]

for z in lines:
	cur3.execute("insert into aa_mypyth (id, data) values (:1, :2 )", lines)
	con.commit()
	
	

cur3.execute('select * from aa_mypyth where id = 19')
	
	
con.close()


"""
OTHER:
def connect(self):
        self.initConnection()
        self.__dsn = cx_Oracle.makedsn(self.hostname, self.port, self.db)
        self.__dsn = utf8encode(self.__dsn)
        self.user = utf8encode(self.user)
        self.password = utf8encode(self.password)

        try:
            self.connector = cx_Oracle.connect(dsn=self.__dsn, user=self.user, password=self.password, mode=cx_Oracle.SYSDBA)
            logger.info("successfully connected as SYSDBA")
        except (cx_Oracle.OperationalError, cx_Oracle.DatabaseError, cx_Oracle.InterfaceError):
            try:
                self.connector = cx_Oracle.connect(dsn=self.__dsn, user=self.user, password=self.password)
            except (cx_Oracle.OperationalError, cx_Oracle.DatabaseError, cx_Oracle.InterfaceError), msg:
                raise SqlmapConnectionException(msg)

        self.initCursor()
        self.printConnected()


"""