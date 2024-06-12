class Function:
    """ implemeting an add, subtract, multiply and divide functions"""

    def add(a,b):
        return a + b

    def subtract(a,b):
        return a - b

    def multiply(a,b):
        return a * b

""" encountering a condition when denominator is zero in else part     """

    def divide(a,b):
        if b != 0:
            return a / b
        else
            return "Error: Division by Zero"
    

class Calculation:
    """      """
    def __init__(self,a,b,Function):
        self.a = a
        self.b = b
        self.Function = Function

    def compute(self):
        """    """
        return self.Function(self.a,self.b)


class CalculationsHistory:

    history = []

    def add_history(x,calculation):
		x.history.append(calculation)

	def get_history(x):
		return x.history

class Calculator:
	
	def __init__(self):
		self.Functions = Function()

	def perform_calculation(self,a,b,function):
		calculation = Calculation(a,b,function)
		result = calculation.compute()
		CalculationsHistory.add_history(calculation)
		return result
	
	def get_calculation_history(self):
		return CalculationHistory.get_history()

calculator = Calculator()
print(calculator.perform_calculation(10,5,Function.add))
print(calculator.perform_calculation(10,5,Function.subtract))
print(calculator.perform_calculation(10,5,Function.multiply))
print(calculator.perform_calculation(10,5,Function.divide))

print(calculator.get_calculation_history())




