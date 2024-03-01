## Юнит-тесты для проектной работы 4-го спринта курса "Автоматизатор тестирования на Python"

### Список реализованных юнит-тестов:

1. `test_set_book_genre_add_genres_return_added_genres`: тест проверяет установку кинге жанра
2. `test_get_books_for_children_add_all_genres_return_children_books`: тест проверяет получение книг для детей, без выдачи рейтинговых жанров (ужасы, детективы)
3. `test_get_book_genre_add_book_return_genre`: тест проверяет получение жанра книги по её имени
4. `test_get_books_with_specific_genre_add_books_all_genres_return_select_genre_books`: тест проверяет получение книг с определённым жанром
5. `test_get_books_genre_add_book_return_book_genre_list_with_added_book`: тест проверяет получение списка books_genre
6. `test_add_book_in_favorites_add_book_return_added_book`: тест проверяет добавление книги в Избранное
7. `test_delete_book_from_favorites_delete_book`: тест проверяет удаление книги из Избранного
8. `test_get_list_of_favorites_books_return_favorites_list`: тест проверяет получение списка Избранных книг
9. `test_add_new_book_name_more_40_symbols_return_empty_dict`: тест проверяет добавление книги в список books_genre с названием более 40 символов
10. `test_add_new_book_twice_return_one_book`: тест проверяет добавление одной и той же книги в список books_genre дважды