from utils import alphabet, compare_numbers


def addition_in_base(num1: str, num2: str, base: int):
    """
    Складывает число в данной СС (2-50).
    Выводит результат с погашовыми объяснениями.
    """
    # Uppercase for consistent symbol handling
    num1 = num1.upper()
    num2 = num2.upper()
    
    # Pad shorter number with leading zeros for visualisation
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    # Giving first steps of the explanation
    explanation = []
    explanation.append(f"Складываем числа в {base}-ичной системе счисления:")
    explanation.append(f" {num1}")
    explanation.append(f"+{num2}")
    explanation.append("-" * (max_len + 2))

    result_digits = []
    carry = 0

    # Doing addition by each digit of the number
    for i in range(max_len - 1, -1, -1):
        d1 = alphabet.index(num1[i])
        d2 = alphabet.index(num2[i])
        total = d1 + d2 + carry

        precarry = carry
        result_digit = total % base
        carry = total // base

        ch1 = num1[i]
        ch2 = num2[i]
        res_char = alphabet[result_digit]

        line = f"{ch1}({d1}) + {ch2}({d2}) + перенос {precarry} = {total} → {res_char} (остаток), перенос: {carry}"
        explanation.append(line)
        result_digits.append(res_char)

    # Adding final carry to the explanation
    if carry > 0:
        explanation.append(f"Остался перенос: {carry} → добавляем в начало")
        result_digits.append(alphabet[carry])

    # Reverse result and return
    result_digits.reverse()
    result = ''.join(result_digits)
    explanation.append("-" * (max_len + 2))
    explanation.append(f"Результат: {result}")

    return result, explanation


def subtraction_in_base(num1: str, num2: str, base: int):
    """
    Вычитает меньшее из большего в данной СС.
    Возвращает результат вычетания и объяснения.
    """
    num1 = num1.upper()
    num2 = num2.upper()

    # Pad the shorter number with leading zeros for visualisation
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    # Starting the explanations
    explanation = []
    explanation.append(f"Вычитаем {num2} из {num1} в {base}-ичной системе счисления:")
    explanation.append(f" {num1}")
    explanation.append(f"-{num2}")
    explanation.append("-" * (max_len + 2))

    result_digits = []
    borrow = 0

    # Substraction by each digit of the number
    for i in range(max_len - 1, -1, -1):
        d1 = alphabet.index(num1[i])
        d2 = alphabet.index(num2[i])
        
        current = d1 - borrow

        if current < d2:
            current += base
            borrow = 1
            explanation.append(
                f"{num1[i]}({d1}) - {num2[i]}({d2}) - заимствование 1 → {current} - {d2} = {current - d2}"
            )
        else:
            borrow = 0
            explanation.append(
                f"{num1[i]}({d1}) - {num2[i]}({d2}) = {current - d2}"
            )

        result_digit = current - d2
        result_digits.append(alphabet[result_digit])

    # Remove leading zeros from the result
    result_digits.reverse()
    result = ''.join(result_digits).lstrip('0') or '0'
    explanation.append("-" * (max_len + 2))
    explanation.append(f"Результат: {result}")

    return result, explanation


def add_multiple_numbers_in_base(numbers: list[str], base: int):
    """
    Складывает список чисел в заданной системе счисления.
    Использует уже реализованную addition_in_base.
    """
    explanation = ["Складываем все частичные произведения:"]
    max_len = max(len(num) for num in numbers)
    total = '0'

    # Выравнивание чисел по длине (слева нулями)
    numbers = [num.zfill(max_len) for num in numbers]

    for i, number in enumerate(numbers):
        explanation.append(f"{i+1}) {number}")

    for number in numbers:
        total, add_expl = addition_in_base(total, number, base)
        explanation += add_expl
        explanation.append(f"Промежуточная сумма: {total}")

    explanation.append(f"Итоговая сумма: {total}")
    return total, explanation




def multiplication_in_base_column(num1: str, num2: str, base: int):
    """
    Поразрядное умножение num1 на num2 в указанной системе счисления (2–50).
    Возвращает результат и объяснение пошагово.
    """
    num1 = num1.upper()
    num2 = num2.upper()

    explanation = []
    explanation.append(f"Поразрядное умножение {num1} × {num2} в {base}-ичной системе:")
    explanation.append("")

    partial_products = []
    num_zeros = 0  # Amount of zeros to add after each step

    for i in range(len(num2) - 1, -1, -1):
        digit2 = alphabet.index(num2[i])
        carry = 0
        row = []
        explanation.append(f"Умножаем на разряд '{num2[i]}' ({digit2}):")

        for j in range(len(num1) - 1, -1, -1):
            digit1 = alphabet.index(num1[j])
            product = digit1 * digit2 + carry
            carry = product // base
            digit_result = product % base
            row.append(alphabet[digit_result])
            explanation.append(
                f"{num1[j]}({digit1}) × {num2[i]}({digit2}) + перенос {carry} = {product} → {alphabet[digit_result]} (перенос {carry})"
            )

        if carry > 0:
            row.append(alphabet[carry])
            explanation.append(f"Добавляем оставшийся перенос: {carry} → {alphabet[carry]}")

        # Reversing the string and adding the zeros to the right
        row.reverse()
        row_str = ''.join(row) + '0' * num_zeros
        partial_products.append(row_str)
        explanation.append(f"Промежуточный результат: {row_str}")
        explanation.append("")

        num_zeros += 1

    # Adding up all the intermediate results
    explanation.append("Складываем все промежуточные результаты:")
    total, add_expl = add_multiple_numbers_in_base(partial_products, base)
    explanation.extend(add_expl)
    explanation.append(f"Окончательный результат: {total}")

    return total, explanation



if __name__ == "__main__":
    """
    Такая же функция как в base_converter.py, для тестов.
    """
    num1 = "5421"
    num2 = "4"
    base = 10
    
    check = compare_numbers(num1, num2, base)
    if check:
        result, steps = addition_in_base(num1, num2, base)

        for line in steps:
            print(line)
        print(f"\nОтвет: {num1} + {num2} в {base}-ичной системе = {result}")
