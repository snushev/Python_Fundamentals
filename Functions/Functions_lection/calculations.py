def calculate(operator: str, num1: int, num2: int):
    if operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        return int(num1 / num2)
    elif operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2


operator = input()
num1 = int(input())
num2 = int(input())
result = calculate(operator, num1, num2)
print(result)