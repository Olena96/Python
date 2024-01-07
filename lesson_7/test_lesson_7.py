from lesson_7.lesson_7 import sort_asc
from lesson_7.lesson_7 import sort_desc
from lesson_7.lesson_7 import sort_words

random_numbers = (7, 2, 9, 4, 1, 8, 5, 3, 10, 6)
random_words = ('Автомобіль', 'Яблуко', 'Веселка', 'Магазин', 'Океан', 'Сонце', 'Гірлянда', 'Папуга',
                'Кавун')


def test_sort_asc():
    assert sort_asc(random_numbers) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_sort_desc():
    assert sort_desc(random_numbers) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def test_sort_words():
    assert sort_words(random_words) == ['Океан', 'Сонце', 'Кавун', 'Яблуко', 'Папуга', 'Веселка',
                                        'Магазин', 'Гірлянда', 'Автомобіль']
