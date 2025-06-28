from base_converter import convert_from_decimal, convert_to_decimal
from operations import addition_in_base, subtraction_in_base, multiplication_in_base_column, add_multiple_numbers_in_base
from utils import alphabet, is_valid, compare_numbers

def get_base(prompt):
    while True:
        try:
            base = int(input(prompt))
            if 2 <= base <= len(alphabet):
                return base
            else:
                print(f"Введите число от 2 до {len(alphabet)}.")
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")


def get_number(prompt, base):
    while True:
        num = input(prompt).strip().upper()
        if is_valid(num, base):
            return num
        else:
            print(f"Число должно содержать только допустимые символы для {base}-ичной системы.")


def print_explanation(explanation):
    print("\nПОШАГОВО:")
    for step in explanation:
        print(step)
    print("-" * 40)


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Перевод чисел")
        print("2. Сложение")
        print("3. Вычитание")
        print("4. Умножение")
        print("5. Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            print("\nПЕРЕВОД ЧИСЛА")
            direction = input("1 - Из другой СС в десятичную\n2 - Из десятичной в другую СС\nВыбор: ").strip()
            if direction == "1":
                base_from = get_base("Введите исходную систему счисления: ")
                num_str = get_number("Введите число: ", base_from)
                result, explanation = convert_to_decimal(num_str, base_from)
                print_explanation(explanation)
                print(f"Ответ: {result}")
            elif direction == "2":
                base_to = get_base("Введите систему счисления для перевода: ")
                try:
                    decimal = int(input("Введите десятичное число: "))
                    result, explanation = convert_from_decimal(decimal, base_to)
                    print_explanation(explanation)
                    print(f"Ответ: {result}")
                except ValueError:
                    print("Ошибка: введите корректное десятичное число.")
            else:
                print("Некорректный выбор.")

        elif choice == "2":
            print("\nСЛОЖЕНИЕ")
            base = get_base("Введите систему счисления: ")
            num1 = get_number("Введите первое число: ", base)
            num2 = get_number("Введите второе число: ", base)
            result, explanation = addition_in_base(num1, num2, base)
            print_explanation(explanation)
            print(f"Ответ: {result}")

        elif choice == "3":
            print("\nВЫЧИТАНИЕ")
            base = get_base("Введите систему счисления: ")
            num1 = get_number("Введите уменьшаемое: ", base)
            num2 = get_number("Введите вычитаемое: ", base)
            if not compare_numbers(num1, num2, base):
                print("Ошибка: первое число должно быть больше или равно второму.")
            else:
                result, explanation = subtraction_in_base(num1, num2, base)
                print_explanation(explanation)
                print(f"Ответ: {result}")

        elif choice == "4":
            print("\nУМНОЖЕНИЕ")
            base = get_base("Введите систему счисления: ")
            num1 = get_number("Введите первое число: ", base)
            num2 = get_number("Введите второе число: ", base)
            if not compare_numbers(num1, num2, base):
                print("Ошибка: первое число должно быть больше или равно второму.")
            else:
                result, explanation = multiplication_in_base_column(num1, num2, base)
                print_explanation(explanation)
                print(f"Ответ: {result}")

        elif choice == "5":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    main()
