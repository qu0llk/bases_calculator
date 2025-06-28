from utils import alphabet, is_valid


def convert_to_decimal(num_str: str, base_from: int):
    """
    Converts a number entered by the user from base_from to decimal (base 10).
    """
    # Making sure the input is in uppercase (relevant for alphabet systems like hex)
    num_str = num_str.upper()
    # A list that will store the full explanation for the user
    explanation = []
    # This will hold the final result in base 10
    total = 0
    # The power to which each digit's base will be raised (starts from the highest digit)
    power = len(num_str) - 1

    # Explaining what we are about to do
    explanation.append(f"Переводим '{num_str}' из {base_from}-ичной в десятичную:")

    # Going through each character in the number
    for i, ch in enumerate(num_str):
        # Finding the numeric value of the current character in the custom alphabet
        digit = alphabet.index(ch)
        # Calculating its value in decimal for the current digit position
        value = digit * (base_from ** power)
        # Explaining this step to the user in detail
        explanation.append(f"{ch} × {base_from}^{power} = {digit} × {base_from**power} = {value}")
        # Adding the calculated value to the total
        total += value
        # Moving to the next lower power
        power -= 1

    # Final explanation line with the total result
    explanation.append(f"Итоговое десятичное число (сумма): {total}")
    return total, explanation



def convert_from_decimal(decimal_number: int, base_to: int):
    """
    Перевод из десятичной СС в base_to введенную пользователем.
    """
    # Making a list which will store all of the explanation that will be given to the user
    explanation = []
    explanation.append(f"Переводим {decimal_number} из десятичной в {base_to}-ичную:")
    
    # Instant answer if decimal is 0
    if decimal_number == 0:
        return "0", explanation + ["Число равно 0, результат: 0"]

    # A list that will store our answer, yet unreversed
    digits = []
    # Making a while statement that will work untill entire number is proccessed
    while decimal_number > 0:
        # Getting the remainder after the devision
        remainder = decimal_number % base_to
        # Converting the remainder to the base_to base for clear explanation
        digit_char = alphabet[remainder]
        # Making a line of explanation, the math one...
        explanation.append(f"{decimal_number} ÷ {base_to} = {decimal_number // base_to}, остаток {remainder} ({digit_char})")
        # Filling in our resulting list with converted remainder
        digits.append(digit_char)
        # Deviding the number, finalizing the proccess
        decimal_number //= base_to

    # Getting the final result of the conversion
    digits.reverse()
    result = ''.join(digits)
    explanation.append(f"Результат: {result}")
    return result, explanation


def convert_number(num_str, base_from, base_to):
    # Checking if user input is valid
    valid, error = is_valid(num_str.upper(), base_from)
    if not valid:
        return None, [error]

    # Addressing functions
    decimal, to_decimal_exp = convert_to_decimal(num_str.upper(), base_from)
    result, from_decimal_exp = convert_from_decimal(decimal, base_to)

    # Returning the result of convertion and adding up the explanation from both convertions
    return result, to_decimal_exp + [""] + from_decimal_exp

if __name__ == "__main__":
    """
    Часть кода для проверки работы этой части полеоцценного кода.
    Проверка для того что-бы эта часть не активировалась при адрессации
    на этот файл из другого файла. Короче, чтоб эта часть запускалась только тогда,
    когда мы запускаем именно этот файл.
    """
    # Imitating user input
    num = "01><(!"
    base_from = 50
    base_to = 13

    # Using the main function to get the result of convertion and the explanation
    result, explanation = convert_number(num, base_from, base_to)
    
    # Making output as preaty as we can
    for line in explanation:
        print(line)
        
    # Final output
    print(f"\nОтвет: {num} из {base_from}-ичной = {result} в {base_to}-ичной")
