# Задача №1 (легша)
# 14 Податки
# Прийшов час податків і вам треба написати програму що б допомогти відділу бугалтерії
# програма приймає від користувача його зарплату за 3 місяці та відсоток який він має сплатити.
# Виведіть на екран скільки треба податків сплатити. Не забудьте ЄСВ(4422)

#OLD
# salary = float(input("Введіть зарплату:"))
# single_tax = float(input("Введіть процент податку:"))
#
# tax_to_pay = (salary * (single_tax / 100)) + 4422
# print(tax_to_pay)

#NEW
# def calculate_tax(salary: int | float, single_tax: int | float):
#     result = (salary * (single_tax / 100)) + 4422
#     return result
#
# #
# # user_salary = float(input("Введіть зарплату:"))
# # user_single_tax = float(input("Введіть процент податку:"))
# #
# # tax_to_pay = calculate_tax(salary=user_salary, single_tax=user_single_tax)
# # print(tax_to_pay)
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

#№OLD
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


# NEW
def add_product(internal_input: str):
    internal_list = internal_input.split()
    print(f"Ось ваш список продуктів: {internal_list}")
    return internal_list


def delete_product(internal_index: int, internal_list: list):
    if 0 < internal_index <= len(internal_list):
        internal_list.pop(internal_index - 1)
        print(f"Ось ваш оновлений список продуктів: {internal_list}")
        return internal_list


def manage_products(user_cart: str):
    user_cart = add_product(internal_input=user_cart)

    while len(user_cart) > 0:
        user_index = int(input("Який продукт ви вже купили?"))
        delete_product(internal_index=user_index, internal_list=user_cart)

    if len(user_cart) == 0:
        user_input = input("Введіть список продуктів через пробіл")
        add_product(internal_input=user_input)
    elif len(user_cart) > 0:
            user_index = int(input("Який продукт ви вже купили?"))
            delete_product(internal_index=user_index, internal_list=user_cart)


user_input = input("Введіть список продуктів через пробіл")
manage_products(user_cart=user_input)
