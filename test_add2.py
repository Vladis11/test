import unittest
import add

class TestAdd(unittest.TestCase):
	
	def test_add(self):
		result = add.add2(10,5)
		self.assertEqual(result,15)
		
if __name__ == '__main__':
	unittest.main()
