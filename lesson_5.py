# Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9
# (включно). (так як робили на уроці).
# Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення).
# і виведіть йому цю табличку.

math_dict = {"+": {}, "*": {}, "-": {}, "/": {}}

for i in range(2, 10):
    for j in range(2, 10):
        math_dict["+"][i, j] = f"{i}+{j}={i+j}"
        math_dict["*"][i, j] = f"{i}*{j}={i*j}"
        math_dict["-"][i, j] = f"{i}-{j}={i-j}"
        math_dict["/"][i, j] = f"{i}/{j}={round((i/j), 2)}"

user_choice = input("Яку таблицю ви хочете бачити? Введіть: '+','-','*' або '/':")

if user_choice in "+/-*":
    for i in math_dict[user_choice]:
        print(math_dict[user_choice][i])
else:
    print("Такої операції немає")


# if user_choice == "+":
#     for i in math_dict["+"]:
#         print(math_dict["+"][i])
# elif user_choice == "*":
#     for i in math_dict["*"]:
#         print(math_dict["*"][i])
# elif user_choice == "-":
#     for i in math_dict["-"]:
#         print(math_dict["-"][i])
# elif user_choice == "/":
#     for i in math_dict["/"]:
#         print(math_dict["/"][i])
# else:
#     print("Такої операції немає")


