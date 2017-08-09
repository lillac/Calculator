class calc(object):
	def __init__(num1, num2):
		self.types = ['add', 'sub', 'mul', 'div']
		self.type = 'add'
		self.num1 = num1
		self.num2 = num2
		
	def calc():
		if (self.type not in self.types):
			print('Error')
			return
		elif (self.type = 'add'):
			return self.num1 + self.num2
		elif (self.type = 'sub'):
			return self.num1 - self.num2
		elif (self.type = 'mul'):
			return self.num1 * self.num2
		elif (self.type = 'div'):
			return self.num1 / self.num2
		

def main():
	a = float(input("1st Number:"))
	b = float(input("2nd NUmber:"))
	m = input("Enter mul for *, div for /, sub for -, add for +.")
	res = calc(a, b)
	res.type = m
	result = res.calc()
	print(result)
	
if __name__ == "__main__":
    main()

