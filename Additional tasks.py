# Задача №1
# Сформуйте стрінг, в якому міститься інформація про певне слово.
# "Word [тут слово] has [тут довжина слова, отримайте з самого слова] letters",
# наприклад "Word 'Python' has 6 letters".
# Для отримання слова для аналізу скористайтеся константою або функцією input().

# word = input("Fill in the word:")
# result = f"Word '{word}' has {len(word)} letters."
# print(result)
#______________________________________________________________________________________________________
# Задача №2
# Напишіть калькулятор, який запитує два числа якщо це множення, додавання, ділення, віднімання.
# Або одне число якщо це
# зняття коріння або піднесення до степіня. Виводить на екран результат.

#Просте рішення:
#Два числа:
# num_1 = int(input("Введіть число №1:"))
# num_2 = int(input("Введіть число №2:"))
# print(f"Результат після додавання двух чисел: {num_1 + num_2}")
# print(f"Результат після віднімання двух чисел: {num_1 - num_2}")
# print(f"Результат після множення двух чисел: {num_1 * num_2}")
# print(f"Результат після ділення двух чисел: {num_1 / num_2}")
#Одне число:
# num_3 = int(input("Введіть число:"))
# print(f"{num_3} в степені 2: {num_3**2}")
# print(f"Квадратний корінь з числа {num_3}: {num_3**0.5}")

#Складне рішення:

# print("Виберіть 1, якщо хочете додати")
# print("Виберіть 2, якщо хочете відняти")
# print("Виберіть 3, якщо хочете помножити")
# print("Виберіть 4, якщо хочете поділити")
# print("Виберіть 5, якщо хочете піднести у степінь")
# print("Виберіть 6, якщо хочете знайти квадратний корінь")
#
# choice = int(input("Яку операцію ви хочете виконати?"))
#
# if choice == 1:
#     num_1 = int(input("Введіть число №1:"))
#     num_2 = int(input("Введіть число №2:"))
#     print(num_1 + num_2)
# elif choice == 2:
#     num_1 = int(input("Введіть число №1:"))
#     num_2 = int(input("Введіть число №2:"))
#     print(num_1 - num_2)
# elif choice == 3:
#     num_1 = int(input("Введіть число №1:"))
#     num_2 = int(input("Введіть число №2:"))
#     print(num_1 * num_2)
# elif choice == 4:
#     num_1 = int(input("Введіть число №1:"))
#     num_2 = int(input("Введіть число №2:"))
#     print(num_1 / num_2)
# elif choice == 5:
#     num_1 = int(input("Введіть число:"))
#     num_2 = int(input("Введіть степінь"))
#     print(num_1 ** num_2)
# elif choice == 6:
#     num_1 = int(input("Введіть число:"))
#     print(num_1 ** 0.5)
# else:
#     print("Такої математичної операції не було")
#______________________________________________________________________________________________________
# Задача №3
# Написати програму, яка просить користувача ввести 4-х значне число з клавіатури,
# після чого повертає це число навпаки.
# Наприклад, користувач вводить 1234, а програма виводить 4321:
# Користувач може ввести будь-яке 4 значне ціле число. Будь-яке 4-х значне число - це число,
# яке складається з 4-х цифр, де кожна цифра може бути від 0 до 9 включно.
# Ваше рішення має це враховувати! Якщо користувач ввів щось не те повідомте йому.
# Варіант 1 Сробуйте вирішити Завдання використовуючи методи поділу (підказка // і %).
# Варіант 2 Сробуйте вирішити Завдання використовуючи індекси.


# user_input = input("Введіть число:")
# print(user_input[::-1], type(user_input))
#
# number = int(user_input)
# digit_1 = number % 10
# digit_2 = (number // 10) % 10
# digit_3 = (number // 100) % 10
# digit_4 = (number // 1000) % 10
#
# reversed_number = digit_1 * 1000 + digit_2 * 100 + digit_3 * 10 + digit_4
# print(f"Число навпаки: {reversed_number}")
#______________________________________________________________________________________________________
# Задача №4
# Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список.
# Тобто, в результаті повинен вийти список із 2-х списків.
# Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
# Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.
# Важливо! Потрібно створити рішення, яке обробляє 3 випадки
# - список порожній, у списку парна кількість елементів і в списку непарна кількість елементів.
#
# Задача №5
# Робимо хештег
# Користувач вводить рядок, ви з цього рядка видаляєте все окрім цифр і букв, додаєте на початок хештег і всі слова пишите з великої літери
#
# Приклади
# привіт№; Всім -> #ПривітВсім
# привіт№; Андрій Петрович -> #АндрійПетрович
