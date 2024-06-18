#1. Write a program that takes two numbers as input and prints their sum.
def sum_of_numbers(num1, num2):
 sum = num1 + num2
 return sum
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = sum_of_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)

#2. Write a python program that checks whether a given number is even or odd.
def check_even_odd(num):
 if num % 2 == 0:
    return "even"
 else:
    return "Odd"
num = int(input("Enter a number: "))
result = check_even_odd(num)
print("The number", num, "is:", result)

#3. Write a python program that calculates the factorial of a given number.
def factorial(num):
 if num == 0 or num == 1:
   return 1
 else:
   fact = 1
 for i in range(2, num + 1):
   fact *= i
   return fact
num = int(input("Enter a number to calculate its factorial: "))
result = factorial(num)
print("The factorial of", num, "is:", result)

#4. Write a program that asks the user for their name and then prints a greeting message.
def greet_user(name):
 print("Hello,", name, "! Welcome to the program.")
name = input("Enter your name: ")
greet_user(name)

#5. Write a program that takes a string input from the user and writes it to a text file.
user_input = input("Enter a string to write to the file: ")
with open('output.txt', 'w') as file:
 file.write(user_input)
print("Input successfully written to 'output.txt' file.")

#6. Write a program that reads the content of a text file and prints it to the console.
with open('input.txt', 'r') as file:
 file_content = file.read()
print("Content of the file 'input.txt':")
print(file_content)

#7. Write a python program that takes a string as input and returns its length.
string = input("Enter a string: ")
length = len(string)
print("The length of the string is:", length)

#8. Write a python program that concatenates two strings and returns the result.
def concatenate_strings(str1, str2):
 concatenated_string = str1 + str2
 return concatenated_string
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = concatenate_strings(string1, string2)
print("The concatenated string is:", result)

#9. Write a python program that checks if a substring is present in a given string.
def check_substring(main_string, substring):
 if substring in main_string:
   return True
 else:
   return False
main_string = input("Enter a main string: ")
substring = input("Enter a substring to check: ")
if check_substring(main_string, substring):
 print("Substring found in the main string.")
else:
 print("Substring not found in the main string.")

#10. Write a python program that converts a given string to uppercase.
string = input("Enter a string: ")
uppercase_string = string.upper()
print("The string in uppercase is:", uppercase_string)

#11. Write a python program that generates the first n numbers in the Fibonacci sequence.
def fibonacci_sequence(n):
 fibonacci = [0, 1]
 for i in range(2, n):
   fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
 return fibonacci[:n]
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_numbers = fibonacci_sequence(n)
print("The first", n, "numbers in the Fibonacci sequence are:", fibonacci_numbers)

#12. Write a python program that calculates the sum of the digits of a given number.
def sum_of_digits(number):
 sum_digits = 0
 while number > 0:
  sum_digits += number % 10
 number //= 10
 return sum_digits
number = int(input("Enter a number to calculate the sum of its digits: "))
result = sum_of_digits(number)
print("The sum of digits of the number", number, "is:", result)

#13. Write a program that asks the user for their birth year and calculates their age.
from datetime import datetime
current_year = datetime.now().year
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print("Your age is:", age)

#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
lines = []
print("Enter lines of text. Enter an empty line to finish:")
while True:
 line = input()
 if line:
   lines.append(line)
 else:
   break
print("Entered lines:")
for line in lines:
 print(line)

#15. Write a program that reads data from a CSV file and prints it to the console.
import csv
filename = 'data.csv'
with open(filename, 'r', newline='') as file:
 reader = csv.reader(file)
 for row in reader:
  print(row)

#16. Write a program in python that counts the frequency of each character in a string.
def count_characters(string):
 char_count = {}
 for char in string:
   if char in char_count:
    char_count[char] += 1
 else:
   char_count[char] = 1
 return char_count
string = input("Enter a string: ")
char_frequency = count_characters(string)
print("Character frequencies in the string:")
for char, freq in char_frequency.items():
 print(f"{char}: {freq}")

#17. Write a program in python that converts a given string to title case (first letter of each word capitalized).
def title_case(string):
 return string.title()
string = input("Enter a string to convert to title case: ")
titlecased_string = title_case(string)
print("The string in title case is:", titlecased_string)

#18. Write a python program that checks if two strings are anagrams of each other.
def are_anagrams(str1, str2):
 return sorted(str1) == sorted(str2)
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if are_anagrams(string1, string2):
 print("The strings are anagrams of each other.")
else:
 print("The strings are not anagrams.")

#19. Write a python program that removes all punctuation from a given string.
import string
def remove_punctuation(string):
 return string.translate(str.maketrans('', '', string.punctuation))
string = input("Enter a string with punctuation: ")
cleaned_string = remove_punctuation(string)
print("String with punctuation removed:", cleaned_string)

#20. Write a python program that takes a list of numbers and returns their sum.
def sum_of_numbers(numbers):
 return sum(numbers)
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = list(map(int, numbers))
result = sum_of_numbers(numbers)
print("The sum of the numbers is:", result)

#21. Write a python program that counts the occurrences of a specific element in a list.
def count_occurrences(lst, element):
 count = 0
 for item in lst:
  if item == element:
   count += 1
 return count

#22. Write a python program that returns the minimum and maximum values in a list of numbers.
def min_max(numbers):
 min_value = min(numbers)
 max_value = max(numbers)
 return min_value, max_value

#23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
def celsius_to_fahrenheit(celsius):
 fahrenheit = (celsius * 9/5) + 32
 return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
 celsius = (fahrenheit - 32) * 5/9
 return celsius
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the temperature unit (C for Celsius, F for Fahrenheit): ")
if unit.upper() == 'C':
 converted_temp = celsius_to_fahrenheit(temperature)
 print(f"{temperature}°C is equal to {converted_temp}°F")
elif unit.upper() == 'F':
 converted_temp = fahrenheit_to_celsius(temperature)
 print(f"{temperature}°F is equal to {converted_temp}°C")
else:
 print("Invalid input. Please enter 'C' or 'F' for the temperature unit.")

#24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
def calculator(num1, num2, operator):
 if operator == '+':
    return num1 + num2
 elif operator == '-':
    return num1 - num2
 elif operator == '*':
    return num1 * num2
 elif operator == '/':
  if num2 != 0:
   return num1 / num2
  else:
   return "Division by zero is not allowed."
 else:
    return "Invalid operator. Please use '+', '-', '*', or '/'."
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
result = calculator(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

#25. Write a program that copies the contents of one text file to another.
def copy_file(source_file, destination_file):
 try:
  with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
    content = source.read()
    destination.write(content)
  print(f"Contents of '{source_file}' successfully copied to '{destination_file}'.")
 except FileNotFoundError:
  print("One of the files does not exist.")

#26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
def check_prefix_suffix(string, prefix, suffix):
 starts_with_prefix = string.startswith(prefix)
 ends_with_suffix = string.endswith(suffix)
 return starts_with_prefix, ends_with_suffix
string = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")
starts_with_prefix, ends_with_suffix = check_prefix_suffix(string, prefix, suffix)
print(f"The string '{string}' starts with '{prefix}': {starts_with_prefix}")
print(f"The string '{string}' ends with '{suffix}': {ends_with_suffix}")

#27. Write a program in python that converts a string into a list of its characters.
def string_to_list(string):
 return list(string)
string = input("Enter a string: ")
characters_list = string_to_list(string)
print(f"The string '{string}' converted to a list of characters is:")
print(characters_list)