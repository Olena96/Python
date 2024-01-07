# Задача 1
# Напишіть програму яка:
# 1. запитує в користувача вартість покупок (amount_product; input; split)
# 2. він їх вводе через пробіл, !!!точна кількість не вказана!!!
# 3. вам потрібно до вартості покупок додати 6,5 відсотки податків (for in)
# 4. потім питаєте чи є в користувача купон на знижку
# 5. якщо є то питаєте це на суму чи на відсоток (if) !Запитати яка сума чи відсоток
# 6. віднімаєте суму або відсоток відповідно від ціни яку отримали раніше
# 7. пишете користувачу кінцеву суму.
#
# * завдання з зірочкою не впливає на бал.
# Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня,
# якщо менше. то тоді просто відкидаємо копійки від ціни.

#import math

# price_str = input().split()
#
# price = []
# for i in price_str:
#     price.append(float(i))
#
# total_sum = sum(price)
# print(f"Загальна сума: {total_sum} грн.")

# tax = 6.5
# total_sum_with_tax = total_sum + ((tax/100) * total_sum)
# print(f"Загальна сума з податком: {total_sum_with_tax} грн.")
#
# coupon = input("У вас є купон? Так/Ні").title()
# if coupon == "Так":
#     coupon_type = input("Який у вас тип купону? Сума/Відсоток").title()
#     if coupon_type == "Сума":
#         coupon_sum = float(input("Введіть суму купону:"))
#         total_after_coupon_sum = total_sum_with_tax - coupon_sum
#         round_total = int((total_after_coupon_sum * 100) % 100)
#         if round_total > 44:
#             total_after_coupon_sum = math.ceil(total_after_coupon_sum)
#         else:
#             total_after_coupon_sum = math.floor(total_after_coupon_sum)
#         print(f"Ваша сума після купону: {total_after_coupon_sum}")
#     elif coupon_type == "Відсоток":
#         coupon_percent = float(input("Введіть відсоток купону:"))
#         total_after_coupon_percent = total_sum_with_tax - (total_sum_with_tax * coupon_percent/100)
#         round_total = int((total_after_coupon_percent * 100) % 100)
#         if round_total > 44:
#             total_after_coupon_percent = math.ceil(total_after_coupon_percent)
#         else:
#             total_after_coupon_percent = math.floor(total_after_coupon_percent)
#         print(f"Ваша сума після купону: { total_after_coupon_percent}")
#     else:
#         print("Ви ввели щось дивне...")
# elif coupon == "Ні":
#     print(f"Жалко. Тоді ваша загальна сума: {total_sum_with_tax} грн.")
# else:
#     print("Ви ввели щось дивне...")
#_____________________________________________________________________________________________________________
# Задача 2
# Уявимо що до нас прийшов наш друг або подруга і попросили написати додаток для покупок в магазині
# що б можна було скласти список продуктів та коли купуєш викреслювати(для викреслення питайте номер елемента,
# що б видалити по індексу треба його передати в pop list_a.pop(0) - видалить нульовий індекс,
# памятайте що користувач не знає що в нас індекси починаються з нуля)
# Також нам відомо що цей список має пять або більше елементів.
# Після кожного видалення елементу виводьте наш оновлений список.
# Після 5 видалень перевірте чи список пустий якщо не пустий напишіть що ось ще є продукти,
# якщо пусти то напишіть про це.

# Також після цього кроку запропонуйте користувачу написати ще продуктів та додати його в кошик.
# і виведіть їх на екран. Але цього разу вже без видалень.

# кроки:
# Спочатку пропонуємо користувачу ввести продукти.
# Робимо 5 запитів на видалення
# Перевіряємо корзину
# Пропонуємо додати продукти
# Виводмо список і прощаємось


# list_products = input("Введіть список продуктів через пробіл").split()
# print(f"Ось ваш список продуктів: {list_products}")
#
# while len(list_products) > 0:
#     del_product = int(input("Який продукт ви вже купили?"))
#     if del_product > 0 and del_product <= len(list_products):
#         list_products.pop(del_product - 1)
#         print(f"Ось ваш оновлений список продуктів: {list_products}")
#
# if len(list_products) == 0:
#     list_products = input("Давайте додамо ще продуктів. Додайте продукти").split()
#     print(f"Ось ваш фінальний список продуктів {list_products}")
# elif len(list_products) > 0:
#     print(f"Ви ще не все купили. Ось що вам залишилось: {list_products}")
# else:
#     print("Такого бути не може")
#_____________________________________________________________________________________________________________
# Задача 3
# Напишіть програму Банкомат.
# Встановіть пін код для користувача(зробимо це константою).
# Запитайте в користувача Пін
# якщо він введе три рази не вірно то напишіть що карта заблокована.
# Використовуйте цикл while.

# PIN = 1234
# max_attempt = 3
# current_attempt = 0
#
# while current_attempt < max_attempt:
#     user_input = int(input("Введіть пароль:"))
#     if user_input == PIN:
#         print("Успішно!")
#         break
#     elif user_input != PIN:
#         print("Невірний пароль!")
#         current_attempt += 1
#
# if current_attempt == max_attempt:
#     print("Карту заблоковано. Зверніться до банку!")
#_____________________________________________________________________________________________________________
# Задача 4
# Напишіть за допомогою f-string та format.
# Дві стрічки де буде підставлятись імя та вік з зміних
# name = "оЛенА"
# age = 21
# f_string = тут ваш код формата ф-стрінг. | повино вийти -> Я Олена, мені 21 рік
# format_string = тут ваш код формата формат стрінг  | повино вийти -> Я Олена, мені 21 рік

# name = "оЛенА"
# age = 21
#
# f_string = f"Я {name.title()}, мені {age}"
# print(f_string)
#
# format_string = "Я {0}, мені {1}".format(name.title(), age)
# format_string = "Я {name}, мені {age}".format(name = name.title(), age = age) #можна і так
# print(format_string)
