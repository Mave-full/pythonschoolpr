from math_operations import add, multiply
from string_operations import split_into_words, count_word_occurrences, add_exclamation

print("Testing math functions:")
print(f"2 + 3 = {add(2, 3)}") 
print(f"2 * 3 = {multiply(2, 3)}")

print("\n=== Тестирование text_processing.py ===")
print(f"Разделение строки: {split_into_words('This is a test')}")  
print(f"Слово 'python' встречается {count_word_occurrences('Python is python PYTHON', 'python')} раза")  
print(f"Добавление восклицания: '{add_exclamation('Hello')}'")  
print(f"Строка уже с '!': '{add_exclamation('Hi!')}'") 
