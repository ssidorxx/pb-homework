""" Логические операции возвращают результаты в булевых (логических) значениях.

Логическая операция and возвращает True, когда и первый и второй операнды истинны.

Логическая операция or возвращает True, если хотя бы один из операндов истинен.

Логическая операция not инвертирует логическое выражение, которому она предшествует. """

name = "John"
age = 17
print(name == "John" or age == 17)  # True если человека зовут John или ему 17

print(not (
            not name == 'John' and not age == 17))  # Напишите логическое выражение со значением "человека зовут John или ему 17" с использованием оператора not

""" Булевы операции не всегда выполняются слева направо! 

Порядок выполнения операций для логических операций следующий: 
not оценивается первым, 
and оценивается следующим, 
or оценивается последним. 
"""

print(name == "John" or not age > 17)  # True если человека зовут John или ему не более 17 лет

# Напишите логическое выражение, проверяющее следующее высказывание: "Человека зовут не John, он старше 20 лет и первая буква его имени не ‘E’".

print(name != 'John' and age > 20 and name[0] != 'E')
