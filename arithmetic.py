def main():
	print("Basic Arithmetic Calculator")

	try:
		first_number = float(input("Enter the first number: "))
		second_number = float(input("Enter the second number: "))
	except ValueError:
		print("Please enter valid numbers.")
		return

	print(f"Addition: {first_number + second_number}")
	print(f"Subtraction: {first_number - second_number}")
	print(f"Multiplication: {first_number * second_number}")
	if second_number == 0:
		print("Division: undefined (cannot divide by zero)")
	else:
		print(f"Division: {first_number / second_number}")


if __name__ == "__main__":
	main()
