import pickle

class Employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno = eno
		self.ename = ename
		self.esal = esal
		self.eaddr = eaddr
	def display(self):
		print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
#pickling
with open('emp.dat','wb') as f:
	e = Employee(100,'durga',1000,'Hyd')
	pickle.dump(e,f)
	print('Pickling of Employee object completed')
#unpickling
with open('emp.dat','rb') as f:
	obj = pickle.load(f)
	print("Employee Information after unpickling")
	obj.display()
