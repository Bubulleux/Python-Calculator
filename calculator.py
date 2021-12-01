from serialaze import FUNCTION, VALUE, UNKNOWN
import math

FUNCTIONS = {
	"+": lambda value: value[0] + value[1],
	"-": lambda value: value[0] - value[1],
	"*": lambda value: value[0] * value[1],
	"/": lambda value: value[0] / value[1],
	"^": lambda value: value[0] ** value[1],
	"sin": lambda value: math.sin(value[0]),
	"cos": lambda value: math.sin(value[0]),
	"tan": lambda value: math.sin(value[0]),
	"sqrt": lambda value: math.sqrt(value[0]),
}

CONSTANTS = {
	"pi": math.pi
}


def calc_formula(formula, unknown=None):
	if unknown is None:
		unknown = {}

	formula_type = formula[0]
	if formula_type == FUNCTION:
		values = [calc_formula(formula_, unknown=unknown) for formula_ in formula[2:]]
		if formula[1] not in FUNCTIONS.keys():
			raise TypeError("Function / Operator doesn't exist")

		return FUNCTIONS[formula[1]](values)
	elif formula_type == VALUE:
		return formula[1]
	elif formula_type == UNKNOWN:
		if formula[1] in unknown:
			return unknown[formula[1]]
		if formula[1] in CONSTANTS:
			return CONSTANTS[1]
		else:
			raise TypeError(f"Value {formula[1]} not found")


