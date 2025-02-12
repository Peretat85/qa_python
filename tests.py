import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

#мой тест №1: позитивные проверки длины названия добавленной книги
    # создаю параметризованный тест
    @pytest.mark.parametrize('name_book', ['Я',
                                            'Мы',
                                            'Капитанская дочка',
                                            'Сказ о мертвой царевне и семи богатырях',
                                            'Проверка названия книги в сорок символов'])
    def test_add_new_book_add_lenght_upto_40(self, name_book):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги с названиями не более 40 символов
        collector.add_new_book(name_book)
        assert name_book in collector.get_books_genre()

#мой тест №2: негативные проверки длины названия добавленной книги
    # создаю параметризованный тест
    @pytest.mark.parametrize('name_book', ['',
                                          'Проверяем название книги длиной 41 символ',
                                          'Проверяем название книги длиной больше сорока символов'])
    def test_add_new_book_add_lenght_more_40(self, name_book):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги с названием не более 40 символов
        collector.add_new_book(name_book)
        assert name_book not in collector.get_books_genre()

#мой тест №3: одну и ту же книгу можно добавить только один раз
    def test_add_new_book_add_double_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Война и мир')
        # определяем длину словаря books_rating, который нам возвращает метод get_books_rating
        l = len(collector.get_books_genre())
        # дублирую книгу
        collector.add_new_book('Война и мир')
        # проверяю, что кол-во записей в словаре не изменилось
        assert len(collector.get_books_genre()) == l

# мой тест №4. проверка добавления жанра для книги
    def test_set_book_genre_genre_for_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.set_book_genre("Десять негритят", "Детективы")
        assert collector.get_book_genre("Десять негритят") == "Детективы"

# мой тест №5. проверка вывода жанра книги по ее имени
    # создаю параметризованный тест
    @pytest.mark.parametrize('name_book, genre', [["Смешарики", "Мультфильмы"],
                                                  ["Горе от ума", "Комедии"],
                                                  ["Птицы", "Ужасы"],
                                                  ["Человек-амфибия", "Фантастика"],
                                                  ["Красная лента", "Детективы"]
                                                  ]
                             )
    def test_get_books_genre_genre_for_book(self, name_book, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)
        assert collector.get_book_genre(name_book) == genre

# мой тест №6. проверка вывода книг определенного жанра
    def test_get_books_with_specific_genre_specific_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        test_list = [["Смешарики", "Мультфильмы"],
                     ["Горе от ума", "Комедии"],
                     ["Птицы", "Мультфильмы"],
                     ["Человек-амфибия","Фантастика"],
                     ["Красная лента","Детективы"]
                     ]
        for list in test_list:
            collector.add_new_book(list[0])
            collector.set_book_genre(list[0],list[1])
        assert collector.get_books_with_specific_genre("Мультфильмы") == ["Смешарики","Птицы"]

# мой тест №7. проверка вывода текущего словаря
    def test_get_books_genre_viewing_dictionary(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # создаем список списков со значениями
        test_list = [["Смешарики", "Мультфильмы"],
                     ["Горе от ума", "Комедии"],
                     ["Птицы", "Мультфильмы"],
                     ["Человек-амфибия", "Фантастика"],
                     ["Красная лента", "Детективы"]
                     ]
        # загоняем список списков в словарь
        for list in test_list:
            collector.add_new_book(list[0])
            collector.set_book_genre(list[0], list[1])
        # проверяем, что все списки встали попарно в словарь
        assert collector.get_books_genre() == {"Смешарики": "Мультфильмы",
                                               "Горе от ума": "Комедии",
                                               "Птицы": "Мультфильмы",
                                               "Человек-амфибия": "Фантастика",
                                               "Красная лента": "Детективы"
                                               }

# мой тест № 8. проверка вывода книг, которые подходят детям
    @pytest.mark.parametrize('name_book, genre', [["Смешарики", "Мультфильмы"],
                                                  ["Горе от ума", "Комедии"],
                                                  ["Человек-амфибия", "Фантастика"]
                                                  ]
                             )
    def test_get_books_for_children_book_withound_ganre_age_reting(self, name_book, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)
        assert name_book in collector.get_books_for_children()

# мой тест № 9. проверка вывода книг, которые не подходят детям
    @pytest.mark.parametrize('name_book, genre', [["Птицы", "Ужасы"],
                                                  ["Красная лента", "Детективы"]
                                                  ])
    def test_get_books_for_children_book_with_ganre_age_reting(self, name_book, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)
        assert name_book not in collector.get_books_for_children()

# мой тест № 10. проверка добавления книги в избранное books_genre
    def test_add_book_in_favorites_book_into_books_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book("Колобок")
        collector.add_book_in_favorites("Колобок")
        assert "Колобок" in collector.get_list_of_favorites_books()

# мой тест № 11. Повторно добавить книгу в избранное нельзя.
    def test_add_new_book_add_double_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book("Колобок")
        # добавляем книгу в избранное
        collector.add_book_in_favorites("Колобок")
        # определяем длину словаря favorites, который нам возвращает метод get_list_of_favorites_books
        l = len(collector.get_list_of_favorites_books())
        # дублирую книгу в избранное
        collector.add_book_in_favorites("Колобок")
        # проверяю, что кол-во записей в словаре не изменилось
        assert len(collector.get_list_of_favorites_books()) == l

# мой тест № 12. Удаление книги из избранного.
    def test_delete_book_from_favorites_books_del(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book("Колобок")
        # добавляем книгу в избранное
        collector.add_book_in_favorites("Колобок")
        # удаляем книгу из избранного
        collector.delete_book_from_favorites("Колобок")
        # проверяю, что в избранном нет книги
        assert "Колобок" not in collector.get_list_of_favorites_books()

# мой тест № 13.  Проверка получения списка избранных книг
    def test_list_of_favorites_books_view_list_favorite(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book("Колобок")
        # добавляем книгу в избранное
        collector.add_book_in_favorites("Колобок")
        assert "Колобок" in collector.get_list_of_favorites_books()
