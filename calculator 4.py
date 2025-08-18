def calculator():
    """
    Простой калькулятор, выполняющий базовые арифметические операции.
    
    Запрашивает у пользователя два числа и операцию (+, -, *, /).
    Возвращает результат вычисления или сообщение об ошибке.
    Обрабатывает ошибки ввода чисел и деление на ноль.
    
    Returns:
        str: Результат вычисления в формате "число1 операция число2 = результат"
             или сообщение об ошибке.
    """
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")
    
    try:
        num1 = float(input("Введите первое число: "))
    except ValueError:
        return "Ошибка: Первое число введено неверно! Введите число."
    
    operation = input("Введите операцию (+, -, *, /): ")
    
    # Проверка допустимой операции
    valid_operations = ['+', '-', '*', '/']
    if operation not in valid_operations:
        return f"Ошибка: Неверная операция! Допустимые операции: {', '.join(valid_operations)}"
    
    try:
        num2 = float(input("Введите второе число: "))
    except ValueError:
        return "Ошибка: Второе число введено неверно! Введите число."
    
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
    
    return f"Результат: {num1} {operation} {num2} = {result:.2f}"

print(calculator())