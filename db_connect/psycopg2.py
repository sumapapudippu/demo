import psycopg2
try:
	con = psycopg2.connect(user='sysadmin',password='',host='127.0.0.1',port='****',database='postgres_db')
	cursor = con.cursor()
	#print PostgreSQL Properties
	print(con.get_dsn_parameters(),'\n')
	#print PostgrSQL version
	cursor.exceute('select version();')
	record = cursor.fetchone()
	print('you are connceted to the -',record,'\n')

except (Exception,psycopg2.Error) as error:
	print('Error while connecting the server PostgreSQL',error)

finally:
	if(connection):
		cursor.close()
		con.close()
		print('PostgreSQL conncetion closed')
	

