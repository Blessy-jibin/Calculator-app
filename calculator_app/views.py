from pyramid.response import Response
from pyramid.view import view_config
from .calculator import Calculator

@view_config(request_method='GET', route_name='home', renderer='json')
def home(request):
	""""""
	return { "result": "Calculator is up" }


@view_config(request_method='GET', route_name='add', renderer='json')
def add(request):
	"""Adds the parameter operands and returns the result"""
	a = request.params['operand1']
	b = request.params['operand2']
	return { "result": Calculator.add(a, b) }

@view_config(request_method='GET', route_name='substract', renderer='json')
def substract(request):
	"""Subtracts the parameter operands and returns the result"""
	a = request.params['operand1']
	b = request.params['operand2']
	return {"result": Calculator.substract(a, b) }
	

@view_config(request_method='GET', route_name='multiply', renderer='json')
def multiply(request):
	"""Multiplies the parameter operands and returns the result"""
	a = request.params['operand1']
	b = request.params['operand2']
	return { "result": Calculator.multiply(a, b)}

@view_config(request_method='GET', route_name='divide', renderer='json')
def divide(request):
	""" Divides the parameter operands and returns the result
		If second operand is zero, raise 400 error"""
	a = request.params['operand1']
	b = request.params['operand2']
	if(float(b) == 0):
			request.response.status = 400
			return {'message': '400 Error-Bad request.Division by zero is not allowed'}
	return {"result": Calculator.divide(a, b)}