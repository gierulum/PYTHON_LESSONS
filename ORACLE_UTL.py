import cx_Oracle
import time

con = cx_Oracle.connect('sys/password@localhost:1521/orcl', mode=cx_Oracle.SYSDBA)

#'localhost:1521/orcl;DBA PRIVILEGE=SYSDBA;PERSIST SECURITY INFO=True;USE')
start  = time.time()
ver = con.version.split(".")
print (ver)
cur = con.cursor()
cur.execute('select * from AA_ABSENCJE')
row = cur.fetchone()




	
	
con.close()
