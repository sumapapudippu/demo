#Python code to demonstrate working of Unittest
import unittest

class TestStringMethods(unittest.TestCase):
	#def setup(self):
    #	pass
	#Returns true if the string contains 4 a	
	def test_strings_a(self):
		self.assertEqual('a'*4,'aaaa')
	#Returns true if the string is in upper case	
	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')
    #Returns true if the string is uppercase 
    #else return False
	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())
	#Return true if the string stripped and matched with the output
	def test_strip(self):
		s='geeksforgeeks'
		self.assertEqual(s.strip('geek'),'sforgeeks')

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(),['hello','world'])
		with self.assertRaises(TypeError):
			s.split(2)


#This allows us to run all of testcode just by running the file
		
if __name__ == '__main__':
	unittest.main()

