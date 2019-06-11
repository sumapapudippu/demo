import pymysql
con = pymysql.connect(host='localhost',database='suma265',user='root',password='12345678')
cursor = con.cursor()
cursor.execute('select * from employees')
record = cursor.fetchone()
print(record)
records = cursor.fetchall()
for record in records:
	print('enter employee name',record[0])
	print('enter employee number',record[1])

records = cursor.fetchmany(3)
#last record details with out using for loop
print('enter employee name',record[2][0])
print('enter employee number',record[2][1])
cursor.close()
connection.close()


	