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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    le_petit_prince = 'Маленький Принц'

    books_and_genres_list = [
        ['Гордость и предубеждение и зомби', 'Ужасы'],
        ['Что делать, если ваш кот хочет вас убить', 'Детективы'],
        ['Гарри Поттер и Филосовский камень', 'Фантастика'],
        ['Двенадцать стульев', 'Комедии'],
        ['Бременские музыканты', 'Мультфильмы']
    ]

    @pytest.mark.parametrize('name, genre', books_and_genres_list)
    def test_set_book_genre_add_genres_return_added_genres(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    def test_get_books_for_children_add_all_genres_return_children_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Бременские музыканты')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Бременские музыканты', 'Мультфильмы')

        result = collector.get_books_for_children()

        assert 'Бременские музыканты' in result and 'Гордость и предубеждение и зомби' not in result

    def test_get_book_genre_add_book_return_genre(self, collector):
        collector.add_new_book(self.le_petit_prince)
        collector.set_book_genre(self.le_petit_prince, 'Мультфильмы')

        expected_result = 'Мультфильмы'

        assert collector.get_book_genre(self.le_petit_prince) == expected_result

    @pytest.mark.parametrize('name, genre', books_and_genres_list)
    def test_get_books_with_specific_genre_add_books_all_genres_return_select_genre_books(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_genre_add_book_return_book_genre_list_with_added_book(self, collector):
        collector.add_new_book(self.le_petit_prince)
        collector.set_book_genre(self.le_petit_prince, 'Мультфильмы')

        expected_result = {self.le_petit_prince: 'Мультфильмы'}

        assert collector.get_books_genre() == expected_result

    def test_add_book_in_favorites_add_book_return_added_book(self, collector):
        collector.add_new_book(self.le_petit_prince)
        collector.add_book_in_favorites(self.le_petit_prince)

        expected_result = ['Маленький Принц']

        assert collector.get_list_of_favorites_books() == expected_result

    def test_delete_book_from_favorites_delete_book(self, collector):
        collector.add_new_book('Ночной Дозор')
        collector.add_new_book('Дневной Дозор')
        collector.add_new_book('Сумеречный Дозор')
        collector.add_book_in_favorites('Ночной Дозор')
        collector.add_book_in_favorites('Дневной Дозор')
        collector.add_book_in_favorites('Сумеречный Дозор')
        collector.delete_book_from_favorites('Дневной Дозор')

        expected_result = ['Ночной Дозор', 'Сумеречный Дозор']

        assert collector.get_list_of_favorites_books() == expected_result

    def test_get_list_of_favorites_books_return_favorites_list(self, collector):
        collector.add_new_book(self.le_petit_prince)
        collector.add_book_in_favorites(self.le_petit_prince)

        expected_result = ['Маленький Принц']

        assert collector.get_list_of_favorites_books() == expected_result

    def test_add_new_book_name_more_40_symbols_return_empty_dict(self, collector):
        name = 'a' * 41
        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    def test_add_new_book_twice_return_one_book(self, collector):
        collector.add_new_book(self.le_petit_prince)
        collector.add_new_book(self.le_petit_prince)

        expected_result = {'Маленький Принц': ''}

        assert collector.get_books_genre() == expected_result
