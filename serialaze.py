import math
NUMBER_CHAR = "1234567890."
SYMBOL_CHAR = "+-*/^()"
VARIABLE_CHAR = "abcdexyz"

NONE_TYPE = -1
NUM_TYPE = 0
SYMBOL_TYPE = 1
LETTER_TYPE = 2

FUNCTION = 0
VALUE = 1
UN_KNOW = 2


SYMBOLS = [["+", "-"], ["*", "/"], ["^"]]
FUNCTIONS = ["sin", "cos", "tan", "sqrt"]


def get_formula(formula_raw):
	formula_raw = clean_formula(formula_raw)
	formula_split = split_formula(formula_raw)

	return get_formula_clean(formula_split)


def get_formula_clean(formula_clean):
	print(formula_clean)
	if len(formula_clean) == 1 and type(formula_clean[0]) is not list:
		element = formula_clean[0]
		if is_number(element):
			return VALUE, float(element)
		else:
			return UN_KNOW, element

	if type(formula_clean[0]) == type([]) and len(formula_clean) == 1:
		formula_clean = formula_clean[0]

	if formula_clean[0] == "(" and formula_clean[-1] == ")":
		formula_clean = formula_clean[1:-1]

	# Check bracket
	inside_bracket = 0
	formula = []
	buffer = []
	for element in formula_clean:
		if element == "(" or element == ")":
			inside_bracket += 1 if element == "(" else -1
			if (inside_bracket != 0 and element == ")") or (inside_bracket != 1 and element == "("):
				buffer += element
			continue

		if inside_bracket == 0:
			if len(buffer) != 0:
				print("Push buffer")
				formula.append(buffer)
				buffer = []
			formula.append(element)
		else:
			buffer.append(element)
	if len(buffer) != 0:
		formula.append(buffer)

	symbol_index = -1
	max_index = len(formula) + 1

	for operators_ in SYMBOLS:
		min_operator = max_index
		for operator_ in operators_:
			if operator_ in formula:
				min_operator = min(min_operator, formula.index(operator_))
		if min_operator != max_index:
			symbol_index = min_operator
			break


	if symbol_index != -1:
		formula_final = (FUNCTION, formula[symbol_index], get_formula_clean(formula[:symbol_index]), get_formula_clean(formula[symbol_index + 1:]))
	elif formula[0] in FUNCTIONS:
		formula_final = (FUNCTION, formula[0], get_formula(formula[1]))
	else:
		formula_final = get_formula_clean(formula[0])

	return formula_final




def clean_formula(formula_raw):
	formula = ""
	for char in formula_raw:
		if char != " ":
			formula += char
	return formula.lower()


def split_formula(formula_raw):
	split_formula = []
	buffer = ""
	buffer_type = NONE_TYPE
	for char in formula_raw:
		type_char = get_type(char)
		if buffer_type != type_char and buffer_type != NONE_TYPE:
			split_formula.append(buffer)
			buffer = ""
			buffer_type = NONE_TYPE

		if type_char == SYMBOL_TYPE:
			split_formula.append(char)
		else:
			buffer += char
			buffer_type = type_char
	if buffer_type != NONE_TYPE:
		split_formula.append(buffer)



	return split_formula


def get_type(char):
	if char in NUMBER_CHAR:
		return NUM_TYPE
	elif char in SYMBOL_CHAR:
		return SYMBOL_TYPE
	elif char.isalpha():
		return LETTER_TYPE
	return NONE_TYPE

def is_number(number:str):
	for char in number:
		if char not in NUMBER_CHAR:
			return False
	if number.count(".") > 1:
		return False
	return True
