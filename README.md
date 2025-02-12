# qa_python

тест № 1: позитивные проверки длины названия добавленной книги: 1, 2, 16, 39,40 символов
test_add_new_book_add_lenght_upto_40

тест №2: негативные проверки длины названия добавленной книги: пусто, 41, 54 символа
test_add_new_book_add_lenght_more_40

тест №3: одну и ту же книгу можно добавить только один раз
test_add_new_book_add_double_books

тест №4. проверка добавления жанра для книги
test_set_book_genre_genre_for_book

тест №5. проверка вывода жанра книги по ее имени
test_get_books_genre_genre_for_book

тест №6. проверка вывода книг определенного жанра
test_get_books_with_specific_genre_specific_genre

тест №7. проверка вывода текущего словаря
test_get_books_genre_viewing_dictionary

тест № 8. проверка вывода книг, которые подходят детям
test_get_books_for_children_book_withound_ganre_age_reting

тест № 9. проверка вывода книг, которые подходят детям
test_get_books_for_children_book_with_ganre_age_reting

тест № 10. проверка добавления книги в избранное books_genre
test_add_book_in_favorites_book_into_books_genre

тест № 11. Повторно добавить книгу в избранное нельзя.
test_add_new_book_add_double_books

тест № 12. Удаление книги из избранного
test_delete_book_from_favorites_books_del

тест № 13.  Проверка получения списка избранных книг
test_list_of_favorites_books_view_list_favorite
