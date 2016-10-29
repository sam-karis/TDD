def try_1(num1, num2, operation):
	if operation == "add":
		return num1 + num2

	elif operation == "subtract":
		return num1 - num2

	elif operation == "multiply":
		return num1 * num2

	elif operation ==  "divide":
		return round(float(num1) / num2, 2)