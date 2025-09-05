import math

def load_history():
    """
    Загружает историю вычислений из файла history.txt.
    
    Returns:
        list: Список строк с историей вычислений.
    """
    history = []
    try:
        with open('history.txt', 'r', encoding='utf-8') as file:
            history = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        pass  # Файл ещё не создан, возвращаем пустой список
    return history

def save_history(history):
    """
    Сохраняет историю вычислений в файл history.txt.
    
    Args:
        history (list): Список строк с историей вычислений.
    """
    with open('history.txt', 'w', encoding='utf-8') as file:
        for calc in history:
            file.write(calc + '\n')

def perform_operation(num1, num2, operation):
    """
    Выполняет арифметическую операцию над двумя числами.
    
    Args:
        num1 (float): Первое число.
        num2 (float): Второе число (игнорируется для sqrt).
        operation (str): Операция (+, -, *, /, ^, sqrt, %).
    
    Returns:
        float: Результат вычисления.
        str: Сообщение об ошибке, если операция недопустима.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Ошибка: Деление на ноль!"
        return num1 / num2
    elif operation == '^':
        return num1 ** num2
    elif operation == 'sqrt':
        if num1 < 0:
            return "Ошибка: Нельзя извлечь квадратный корень из отрицательного числа!"
        return math.sqrt(num1)
    elif operation == '%':
        return (num1 * num2) / 100

def calculator():
    """
    Простой калькулятор, выполняющий базовые арифметические операции.
    
    Запрашивает у пользователя два числа и операцию (+, -, *, /, ^, sqrt, %).
    Для операции sqrt используется только первое число, второе игнорируется.
    Для операции % вычисляется num1 процентов от num2.
    Цикл позволяет выполнять многократные вычисления.
    Выход возможен через ввод 'выход', 'q' или 'exit' вместо числа или операции.
    История вычислений сохраняется в файл history.txt, доступна через команду 'history'.
    Команда 'clear' очищает историю вычислений, 'last' показывает последнее вычисление.
    
    Returns:
        None: Выводит результаты вычислений в консоль.
    """
    history = load_history()  # Загружаем историю из файла
    
    print("=" * 50)
    print("Простой калькулятор".center(50))
    print("Доступные операции: +, -, *, /, ^, sqrt, %".center(50))
    print("Команды: 'history' для истории, 'clear' для очистки, 'last' для последнего результата, 'выход', 'q', 'exit'.".center(50))
    print("=" * 50)
    
    while True:
        print("\n" + "-" * 50)
        num1_input = input("Введите первое число (или 'выход', 'q', 'exit' для завершения): ")
        if num1_input.lower() in ['выход', 'q', 'exit']:
            save_history(history)  # Сохраняем историю перед выходом
            print("\n" + "=" * 50)
            print("Работа калькулятора завершена.".center(50))
            print("=" * 50)
            break
        
        try:
            num1 = float(num1_input)
        except ValueError:
            print("\nОшибка: Первое число введено неверно! Введите число.".center(50))
            continue
        
        operation = input("Введите операцию (+, -, *, /, ^, sqrt, %, 'history', 'clear', 'last', 'выход', 'q', 'exit'): ")
        
        # Проверка на выход
        if operation.lower() in ['выход', 'q', 'exit']:
            save_history(history)  # Сохраняем историю перед выходом
            print("\n" + "=" * 50)
            print("Работа калькулятора завершена.".center(50))
            print("=" * 50)
            break
        
        # Проверка команды history
        if operation.lower() == 'history':
            print("\n" + "=" * 50)
            if history:
                print("История вычислений:".center(50))
                for calc in history:
                    print(calc.center(50))
            else:
                print("История вычислений пуста.".center(50))
            print("=" * 50)
            continue
        
        # Проверка команды clear
        if operation.lower() == 'clear':
            history.clear()
            save_history(history)  # Очищаем файл истории
            print("\n" + "=" * 50)
            print("История вычислений очищена.".center(50))
            print("=" * 50)
            continue
        
        # Проверка команды last
        if operation.lower() == 'last':
            print("\n" + "=" * 50)
            if history:
                print("Последнее вычисление:".center(50))
                print(history[-1].center(50))
            else:
                print("История вычислений пуста.".center(50))
            print("=" * 50)
            continue
        
        # Проверка допустимой операции
        valid_operations = ['+', '-', '*', '/', '^', 'sqrt', '%']
        if operation not in valid_operations:
            print(f"\nОшибка: Неверная операция! Допустимые операции: {', '.join(valid_operations)}".center(50))
            continue
        
        # Для sqrt второе число не требуется, но запрашиваем для единообразия
        if operation != 'sqrt':
            try:
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("\nОшибка: Второе число введено неверно! Введите число.".center(50))
                continue
        else:
            num2 = 0  # Второе число не используется для sqrt
        
        # Выполнение операции
        result = perform_operation(num1, num2, operation)
        
        # Если результат — строка (ошибка), выводим её
        if isinstance(result, str):
            print(f"\n{result}".center(50))
        else:
            # Формируем строку результата
            result_str = f"Результат: {num1} {operation} {num2 if operation != 'sqrt' else ''} = {result:.2f}"
            print(f"\n{result_str}".center(50))
            # Сохраняем успешное вычисление в историю
            history.append(result_str)
            save_history(history)  # Сохраняем историю в файл
        print("-" * 50)

if __name__ == "__main__":
    calculator()