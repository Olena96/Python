# Створіть два файли
# в 1-му напишіть такі функції:
# 1) сортування списка по зростанню числа, від меншого до більшого.
# Функція приймає список з чисел і повертає відсортований список.
# 2) сортування списка на спад, від  більшого до меншого.
# Функція приймає список з чисел і повертає відсортований список.
# 3) сортування за кількістю букв у слові.
# Функція приймає список з слів і повертає відсортований список.
#
# 2-ий файл з трьома тестами який буде тестити ці три функції.
# В кожному тесті 1 тест.
# В тестових функціях ми ставимо типізацію.
# В першому файлі в всіх функціях проставляємо що приймає і що повертає.
# Встановіть собі пайтест і прораньте.
# До домашки отрім кода додайте скріншот прогона тестів.



def sort_asc(list_numbers: list) -> list:
    sorted_numbers = sorted(list_numbers)
    return sorted_numbers


# cпробувала заюзати *args
def sort_args(*args) -> list:
    sorted_numbers = sorted(args)
    return sorted_numbers


def sort_desc(list_numbers: list) -> list:
    sorted_numbers = sorted(list_numbers, reverse=True)
    return sorted_numbers


def sort_words(list_words: list) -> list:
    sorted_words = sorted(list_words, key=len)
    return sorted_words


random_numbers = [7, 2, 9, 4, 1, 8, 5, 3, 10, 6]
random_words = ['Автомобіль', 'Яблуко', 'Веселка', 'Магазин', 'Океан', 'Сонце', 'Гірлянда', 'Папуга',
                'Кавун']

print(sort_asc(list_numbers=random_numbers))
print(sort_args(7, 2, 9, 4, 1, 8, 5, 3, 10, 6))
print(sort_desc(list_numbers=random_numbers))
print(sort_words(list_words=random_words))
