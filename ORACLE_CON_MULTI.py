import cx_Oracle

con = cx_Oracle.connect('sys/Leopold666@localhost:1521/orcl', mode=cx_Oracle.SYSDBA)
cur = con.cursor()
cur.execute('select * from AAA_PUSTA order by id')

print ('PRINT MULTIROWS HERE (1 query): ')
for result in cur:
    print (result)
cur.close()

cur1 = con.cursor()
cur1.prepare('select * from AAA_PUSTA where id = :id')
cur1.execute(None, {'id': 1})
res = cur1.fetchall()
print ('PRINT MULTIROWS HERE (2 query - first id check): ')
print (res)
cur1.execute(None, {'id': 2})

print ('PRINT MULTIROWS HERE (2 query - second id check): ')
res2 = cur1.fetchall()
print (res2)

print ('PRINT RESULTS FROM RESULT (RESI): ')
for resi in res2:
	print (resi)
	print (resi[2])
	res_orcl = resi[2]
	print ('PRINT ORCL VARIABLE BELOW: ')
	print (res_orcl)

cur_resi = con.cursor()

print ('PRINT (2) ORCL VARIABLE BELOW: ')
print (res_orcl)


cur_resi.prepare('select * from AAA_PUSTA where surname = :surname')
cur_resi.execute(None, {'surname': res_orcl})
result_orcl = cur_resi.fetchall()
print ('PRINT THE QUERY WITH VARIABLE BELOW: ')
print (result_orcl)

cur_resi.close()
cur1.close()

cur2 = con.cursor()
func_orcl = cur2.callfunc('aa_puste', cx_Oracle.NUMBER, ('abc', 2))
print (func_orcl)
cur2.close

con.close()    
