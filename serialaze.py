NUMBER_CHAR = "1234567890."
SYMBOL_CHAR = "+-*/^()"
VARIABLE_CHAR = "abcdexyz"

NONE_TYPE = -1
NUM_TYPE = 0
SYMBOL_TYPE = 1
LETTER_TYPE = 2

FUNCTION = 0
VALUE = 1
UNKNOWN = 2

SYMBOLS = [["+", "-"], ["*", "/"], ["^"]]
OPERATORS = [operator_ for _operators in SYMBOLS for operator_ in _operators]
FUNCTIONS = ["sin", "cos", "tan", "sqrt"]


def get_formula(formula_raw):
	formula_raw = clean_formula(formula_raw)
	formula_split = split_formula(formula_raw)
	check_result = check_syntax(formula_split)
	if check_result is not None:
		raise TypeError(check_result)
	syntax_clean = make_syntax_clean(formula_split)
	print(syntax_clean)

	return get_formula_clean(syntax_clean)


def get_formula_clean(formula_clean):
	print(formula_clean)
	if len(formula_clean) == 1 and type(formula_clean[0]) is not list:
		element = formula_clean[0]
		if is_number(element):
			return VALUE, float(element)
		else:
			return UNKNOWN, element

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

	for operators_ in SYMBOLS:
		max_operator = -1
		for operator_ in operators_:
			if operator_ in formula:
				max_operator = max(max_operator, get_last_occurrence(formula, operator_))
		if max_operator != -1:
			symbol_index = max_operator
			break

	if symbol_index != -1:
		formula_final = (FUNCTION, formula[symbol_index], get_formula_clean(formula[:symbol_index]),
						 get_formula_clean(formula[symbol_index + 1:]))
	elif formula[0] in FUNCTIONS:
		formula_final = (FUNCTION, formula[0], get_formula(formula[1]))
	else:
		formula_final = get_formula_clean(formula[0])

	return formula_final


def get_last_occurrence(list_input, element_found):
	last_occurrence_index = -1
	for i, e in enumerate(list_input):
		if e == element_found:
			last_occurrence_index = i

	return last_occurrence_index


def make_syntax_clean(formula):
	final_formula = []
	previous_type = -1
	previous_char = ""
	for i, e in enumerate(formula):
		cur_type = get_type(e)
		if (e == "-" or e == "+") and (previous_char == "(" or previous_char == ""):
			final_formula.append("0")

		if (e == "(" or cur_type == LETTER_TYPE) and previous_char not in OPERATORS and previous_type != -1 and previous_char not in FUNCTIONS:
			final_formula.append("*")
		final_formula.append(e)
		previous_char = e
		previous_type = cur_type

	return final_formula


def check_syntax(formula):
	print(OPERATORS)

	if get_type(formula[0]) in OPERATORS and formula[0] != "-":
		return "Fist Element can be an operator"
	if get_type(formula[-1]) in OPERATORS:
		return "Last Element can be an operator"

	for i, e in enumerate(formula):
		if e in OPERATORS and (formula[i - 1] in OPERATORS or formula[i + 1] in OPERATORS):
			return "Tow operator cannot follow each other"

		if e in FUNCTIONS and formula[i + 1] != "(":
			return "You a bracket after a function"

	return None


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


def is_number(number: str):
	for char in number:
		if char not in NUMBER_CHAR:
			return False
	if number.count(".") > 1:
		return False
	return True
