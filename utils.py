alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()[]<>"

def is_valid(num_str: str, base: int):
    """
    Проверяем, правильное совпадает ли СС введенного числа с той системой,
    которая была введена "пятикласником".
    Программа будет останавливать работу на первом же символе из не интересующей СС.
    """
    valid_chars = alphabet[:base]
    for ch in num_str:
        if ch not in valid_chars:
            return False, f"Недопустимый символ '{ch}' для системы счисления с основанием {base}."
    return True, ""

def compare_numbers(num1: str, num2: str, base: int) -> bool:
    """
    Проверка, больше ли num1, чем num2.
    Возвращает True если num1 больше, иначе False.
    """
    if base == 10:
        return int(num1) > int(num2)

    num1 = num1.upper().lstrip('0')
    num2 = num2.upper().lstrip('0')

    if len(num1) > len(num2):
        return True
    elif len(num1) < len(num2):
        return False

    for ch1, ch2 in zip(num1, num2):
        d1 = alphabet.index(ch1)
        d2 = alphabet.index(ch2)
        if d1 > d2:
            return True
        elif d1 < d2:
            return False

    # Они равны
    return False  # <--- вот тут была логическая ошибка
