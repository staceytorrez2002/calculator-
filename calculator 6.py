import math

def calculator():
    """
    Простой калькулятор, выполняющий базовые арифметические операции.
    
    Запрашивает у пользователя два числа и операцию (+, -, *, /, ^, sqrt).
    Для операции sqrt используется только первое число, второе игнорируется.
    Возвращает результат вычисления или сообщение об ошибке.
    Обрабатывает ошибки ввода чисел и деление на ноль.
    
    Returns:
        str: Результат вычисления в формате "число1 операция число2 = результат"
             или сообщение об ошибке.
    """
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /, ^, sqrt")
    
    try:
        num1 = float(input("Введите первое число: "))
    except ValueError:
        return "Ошибка: Первое число введено неверно! Введите число."
    
    operation = input("Введите операцию (+, -, *, /, ^, sqrt): ")
    
    # Проверка допустимой операции
    valid_operations = ['+', '-', '*', '/', '^', 'sqrt']
    if operation not in valid_operations:
        return f"Ошибка: Неверная операция! Допустимые операции: {', '.join(valid_operations)}"
    
    # Для sqrt второе число не требуется, но запрашиваем для единообразия
    if operation != 'sqrt':
        try:
            num2 = float(input("Введите второе число: "))
        except ValueError:
            return "Ошибка: Второе число введено неверно! Введите число."
    else:
        num2 = 0  # Второе число не используется для sqrt
    
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
    elif operation == '^':
        result = num1 ** num2
    elif operation == 'sqrt':
        if num1 < 0:
            return "Ошибка: Нельзя извлечь квадратный корень из отрицательного числа!"
        result = math.sqrt(num1)
    
    return f"Результат: {num1} {operation} {num2 if operation != 'sqrt' else ''} = {result:.2f}"

print(calculator())