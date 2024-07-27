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
        collector = BooksCollector()
    # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    # проверяем, что добавилось именно две
    # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    @pytest.mark.parametrize('name', ['Пила', 'Логика'])
    def test_add_new_book_add_book_in_dict(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', ['', 'x' * 41])
    def test_add_new_book_not_adding_book_in_dict(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    @pytest.mark.parametrize('name, genre', [['Пила', 'Ужасы'], ['Пираты карибского моря', 'Фантастика']])
    def test_set_book_genre_set_valid_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [['Сборник стихотворений', 'Проза'], ['Развал СССР', 'Политика']])
    def test_set_book_genre_not_set_valid_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) != genre

    @pytest.mark.parametrize("name, genre", [
        ['Гарри Поттер', 'Фантастика'],
        ['Война и мир', None]
    ])
    def test_get_book_genre_get_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize("genre, name", [
        ['Фантастика', ['Гарри Поттер']],
        ['Ужасы', []],
    ])
    def test_get_books_with_specific_genre_list_book(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_with_specific_genre(genre) == name

    def test_get_books_genre_get_genre_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Ну погоди!')
        collector.set_book_genre('Ну погоди!', 'Мультфильмы')
        books_genre = collector.get_books_genre()
        assert len(books_genre) == 1
        assert books_genre['Ну погоди!'] == 'Мультфильмы'

    def test_get_books_for_children_books_specialy_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Штамм')
        collector.set_book_genre('Штамм', 'Ужасы')
        collector.add_new_book('Незнайка на луне')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
        children_books = collector.get_books_for_children()
        assert len(children_books) == 1
        assert 'Незнайка на луне' in children_books

    def test_add_book_in_favorites_add_book_in_favorites_list(self):
        collector = BooksCollector()
        collector.add_new_book('Каратель')
        collector.add_book_in_favorites('Каратель')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert 'Каратель' in favorites

    def test_delete_book_from_favorites_delite_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Логика')
        collector.add_book_in_favorites('Логика')
        collector.delete_book_from_favorites('Логика')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 0

    def test_get_list_of_favorites_books_displaying_books_infavorites(self):
        collector = BooksCollector()
        collector.add_new_book('Штамм')
        collector.add_book_in_favorites('Штамм')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1
