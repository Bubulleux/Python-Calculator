from serialaze import FUNCTION, VALUE, UN_KNOW
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
}

def calc_formula(formula, un_know=None):
	if un_know is None:
		un_know = {}

	formula_type = formula[0]
	if formula_type == FUNCTION:
		values = (calc_formula(formula_) for formula_ in  formula[2:])
		return


