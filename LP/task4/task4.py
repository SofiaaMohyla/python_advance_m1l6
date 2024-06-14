def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def sort_strings_by_length(strings):
    return sorted(strings, key=len)


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def celsius_to_fahrenheit(celsius):
    return (celsius - 32) * 5 / 9


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
