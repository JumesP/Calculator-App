def add(num1, num2):
    answer = num1 + num2
    return answer

def sub(num1, num2):
    answer = num1 - num2
    return answer

def multiply(num1, num2):
    answer = num1 * num2
    return answer

def divide(num1, num2):
    answer = num1 / num2
    return answer

def calculate(num1, num2, operator):
    num1, num2 = float(num1), float(num2)
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return sub(num1, num2)
    elif operator == "%":
        return divide(num1, num2)
    elif operator == "x":
        return multiply(num1, num2)

def alt_calculate(num1, num2, operator):
    num1, num2 = int(num1), int(num2)
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "%":
        return num1 / num2
    elif operator == "x":
        return num1 * num2