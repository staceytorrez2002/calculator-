def calculator():
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")
    
    try:
        num1 = float(input("Введите первое число: "))
        operation = input("Введите операцию (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Ошибка: Деление на ноль!"
            result = num1 / num2
        else:
            return "Ошибка: Неверная операция!"
        
        return f"Результат: {num1} {operation} {num2} = {result:.2f}"
    
    except ValueError:
        return "Ошибка: Введите числа!"

# Запускаем калькулятор
print(calculator())