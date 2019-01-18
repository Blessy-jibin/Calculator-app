from pyramid.response import Response
from pyramid.view import view_config
from .calculator import Calculator
from pyramid.httpexceptions import exception_response

@view_config(route_name='home')
@view_config(route_name='calculator')
def home(request):
	"""Returns response with staus code 200"""
	raise exception_response(200, explanation="Calculator is up and running")


@view_config(request_method='GET', route_name='add', renderer='json')
def add(request):
	"""Adds the parameter operands and returns the result"""
	a = request.params['operand1']
	b = request.params['operand2']
	# if one of the operand is missing raise 400 error
	if(not(a) or not(b)):
		raise exception_response(400, explanation="Operand1 and operand2 are required to perform operation")
	return { "result": Calculator.add(a, b) }

@view_config(request_method='GET', route_name='substract', renderer='json')
def substract(request):
	"""Subtracts the parameter operands and returns the result"""
	a = request.params['operand1']
	b = request.params['operand2']
	# if one of the operand is missing raise 400 error
	if(not(a) or not(b)):
		raise exception_response(400, explanation="Operand1 and operand2 are required to perform operation")
	return {"result": Calculator.substract(a, b) }
	

@view_config(request_method='GET', route_name='multiply', renderer='json')
def multiply(request):
	"""Multiplies the parameter operands and returns the result"""
	a = request.params['operand1']
	b = request.params['operand2']
	# if one of the operand is missing raise 400 error
	if(not(a) or not(b)):
		raise exception_response(400, explanation="Operand1 and operand2 are required to perform operation")
	return { "result": Calculator.multiply(a, b)}

@view_config(request_method='GET', route_name='divide', renderer='json')
def divide(request):
	""" Divides the parameter operands and returns the result
		If second operand is zero, raise 400 error"""
	a = request.params['operand1']
	b = request.params['operand2']
	# if one of the operand is missing raise 400 error
	if(not(a) or not(b)):
		raise exception_response(400, explanation="Operand1 and operand2 are required to perform operation")
	if(float(b) == 0):
			raise exception_response(400, explanation="Division by zero is not possible")
	return {"result": Calculator.divide(a, b)}