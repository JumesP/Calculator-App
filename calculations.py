from main import num1, num2, operator

def add(num1, num2):
    answer = num1 + num2
    return answer

def sub(num1, num2):
    answer = num1 / num2
    return answer

def multiply(num1, num2):
    answer = num1 * num2
    return answer

def divide(num1, num2):
    answer = num1 / num2
    return answer

def calculate(num1, num2, operator):
    if operator == "add":
        return add(num1, num2)
    elif operator == "sub":
        return sub(num1, num2)
    elif operator == "multiply":
        return multiply(num1, num2)
    elif operator == "divide":
        return divide(num1, num2)