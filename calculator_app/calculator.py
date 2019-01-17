class Calculator:
	''' This is class for doing mathematical operations'''

	def add(a, b):
		"""
		Additon operation

		Keyword arguments:
			a -- the first operand
			b -- the second operand

		Returns:
			a+b
		"""
		return float(a) + float(b)

	def substract(a, b):
		"""
		Substraction operation

		Keyword arguments:
			a -- the first operand
			b -- the second operand

		Returns:
			a-b
		"""
		return float(a) - float(b)

	def multiply(a, b):
		"""
		Multiplication operation 

		Keyword arguments:
			a -- the first operand
			b -- the second operand

		Returns:
			a*b
		"""
		return float(a) * float(b)

	def divide(a, b):
		"""
		Division operation 

		Keyword arguments:
		a -- the first operand
		b -- the second operand

		Returns:
			a/b
		"""
		return float(a) / float(b)