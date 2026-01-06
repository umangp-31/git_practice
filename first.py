import math
import random
import time

def add(a=30, b=45):
    return a + b


def subtract(a, b):
    return f"Substract is :{a - b}"


def multiply(a, b):
    return f"Multiplication is :{a * b}"


def divide(a, b):
    if b == 0:
        return None
    return a / b


def reverse_string(text):
    return text[::-1]


def capi_words(sentence):
    print( " ".join(word.capitalize() for word in sentence.split()))


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def find_max(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def find_min(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def remove_duplicates(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


def generate_random_numbers(count, start=1, end=100):
    numbers = []
    for _ in range(count):
        numbers.append(random.randint(start, end))
    return numbers


def generate_random_string(length):
    chars = "aaaaaaaaaaaaaaaa"
    result = ""
    for _ in range(length):
        result += random.choice(chars)
    return result


def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_sum(numbers=0):
    total = 0
    for num in numbers:
        total += num
    return total


def filter_even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens


def read_file_mock(filename):
    print(f"Reading file: {filename}")
    return ["line1", "line2", "line3"]


def write_file_mock(filename, content):
    print(f"Writing to file: {filename}")
    for line in content:
        print(line)


def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def delay(seconds):
    time.sleep(seconds)

def process_data():
    numbers = generate_random_numbers(10)
    print("Numbers:", numbers)

    avg = calculate_average(numbers)
    print("Average:", avg)

    primes = [n for n in numbers if is_prime(n)]
    print("Prime Numbers:", primes)

    evens = filter_even_numbers(numbers)
    print("Even Numbers:", evens)


def process_strings():
    text = generate_random_string(10)
    print("Original:", text)
    print("Reversed:", reverse_string(text))
    print("Vowel Count:", count_vowels(text))


def main():
    print("Program Started")
    print("Current Time:", get_current_time())

    process_data()
    process_strings()
    capi_words("Hello World")
    print("Factorial of 5:", factorial(5))
    print("Is 10 Even?", is_even(10))
    print("Is 17 Prime?", is_prime(17))

    print("Program Finished")


if __name__ == "__main__":
    main()
