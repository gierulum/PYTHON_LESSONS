import cx_Oracle
import sys

con = cx_Oracle.connect('sys/Leopold666@localhost:1521/orcl', mode=cx_Oracle.SYSDBA)
proced = con.cursor()

try:
	proced.callproc('pusta_dane')
	print ('procedura zostala wykonana!!')
except ValueError:
	print ('OPS!! THERE IS AN ERROR... Try again ;P', sys.exc_info())
proced.close()
procarg = con.cursor()
myvar = procarg.var(cx_Oracle.NUMBER)


try:
	call_pr_arg = procarg.callproc('dodaj', (4,5))
	print (call_pr_arg)
	print ('Procedura z argumentami wykonana poprawnie!!')
except ValueError:
	print ('OPS!! THERE IS AN ERROR IN ARG PROC... Try again ;P', sys.exc_info())
procarg.close()

	
con.close()    
