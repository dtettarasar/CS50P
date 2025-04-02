expression = input("Expression: ").split(" ")

first_int = float(expression[0])
second_int = float(expression[2])
operation = expression[1]

# print(f"first int: {first_int}")
# print(f"second_int: {second_int}")
# print(f"operation: {operation}")

result = None

match operation:

    case "+":
        # print("addition")
        result = first_int + second_int

    case "-":
        # print("soustraction")
        result = first_int - second_int

    case "*":
        # print("multiplication")
        result = first_int * second_int

    case "/":
        # print("division")
        result = first_int / second_int

result = round(result, 1)

print(result)
