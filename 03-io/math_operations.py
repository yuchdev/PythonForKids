def addition(first_number, second_number):
    addition_result = first_number + second_number
    return addition_result


def subtract(first_number, second_number):
    subtraction_result = first_number - second_number
    return subtraction_result


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operation = int(input("Enter operation code (): 1 for addition, 2 for subtraction: "))

if operation == 1:
    print("Operation you choose is addition")
    result = addition(number1, number2)
if operation == 2:
    print("Operation you choose is subtraction")
    result = subtract(number1, number2)
else:
    print("Next time choose correct number please")


print(f"First number is {number1}")
print(f"Second number is {number2}")
print(f"Operation is {operation}")
print(f"Result is {result}")
