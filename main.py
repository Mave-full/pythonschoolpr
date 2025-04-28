from math_operations import add, multiply
from string_operations import capitalize_string, reverse_string

print("тест математических функций:")
print(f"2 + 3 = {add(2, 3)}")  
print(f"2 * 3 = {multiply(2, 3)}")  

print("\nтест строковых функций:")
print(f"'hello' capitalized: '{capitalize_string('hello')}'") 
print(f"'hello' reversed: '{reverse_string('hello')}'")