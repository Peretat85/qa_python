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

PS C:\Users\peret\qa_python> pytest -v tests.py
=================================================== test session starts ====================================================
platform win32 -- Python 3.11.2, pytest-8.3.4, pluggy-1.5.0 -- C:\Users\peret\AppData\Local\Programs\Python\Python311\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\peret\qa_python
plugins: cov-6.0.0
collected 26 items                                                                                                          

tests.py::TestBooksCollector::test_add_new_book_add_two_books PASSED                                                  [  3%] 
tests.py::TestBooksCollector::test_add_new_book_add_lenght_upto_40[\u042f] PASSED                                     [  7%] 
tests.py::TestBooksCollector::test_add_new_book_add_lenght_upto_40[\u041c\u044b] PASSED                               [ 11%] 
tests.py::TestBooksCollector::test_add_new_book_add_lenght_upto_40[\u041a\u0430\u043f\u0438\u0442\u0430\u043d\u0441\u043a\u0430\u044f \u0434\u043e\u0447\u043a\u0430] PASSED [ 15%]
tests.py::TestBooksCollector::test_add_new_book_add_lenght_upto_40[\u0421\u043a\u0430\u0437 \u043e \u043c\u0435\u0440\u0442\u
0432\u043e\u0439 \u0446\u0430\u0440\u0435\u0432\u043d\u0435 \u0438 \u0441\u0435\u043c\u0438 \u0431\u043e\u0433\u0430\u0442\u044b\u0440\u044f\u0445] PASSED [ 19%]
tests.py::TestBooksCollector::test_add_new_book_add_lenght_upto_40[\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043d\u0
430\u0437\u0432\u0430\u043d\u0438\u044f \u043a\u043d\u0438\u0433\u0438 \u0432 \u0441\u043e\u0440\u043e\u043a \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432] PASSED [ 23%]
tests.py::TestBooksCollector::test_add_new_book_add_lenght_more_40[] PASSED                                           [ 26%]
tests.py::TestBooksCollector::test_add_new_book_add_lenght_more_40[\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0435\u043c \u0
43d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u0438\u0433\u0438 \u0434\u043b\u0438\u043d\u043e\u0439 41 \u0441\u0438\u043c\u0432\u043e\u043b] PASSED [ 30%]
tests.py::TestBooksCollector::test_add_new_book_add_lenght_more_40[\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0435\u043c \u0
43d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u0438\u0433\u0438 \u0434\u043b\u0438\u043d\u043e\u0439 \u0431\u043
e\u043b\u044c\u0448\u0435 \u0441\u043e\u0440\u043e\u043a\u0430 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432] PASSED [ 34%]
tests.py::TestBooksCollector::test_add_new_book_add_double_books PASSED                                               [ 38%] 
tests.py::TestBooksCollector::test_set_book_genre_genre_for_book PASSED                                               [ 42%] 
tests.py::TestBooksCollector::test_get_books_genre_genre_for_book[\u0421\u043c\u0435\u0448\u0430\u0440\u0438\u043a\u0438-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED [ 46%]
tests.py::TestBooksCollector::test_get_books_genre_genre_for_book[\u0413\u043e\u0440\u0435 \u043e\u0442 \u0443\u043c\u0430-\u041a\u043e\u043c\u0435\u0434\u0438\u0438] PASSED [ 50%]
tests.py::TestBooksCollector::test_get_books_genre_genre_for_book[\u041f\u0442\u0438\u0446\u044b-\u0423\u0436\u0430\u0441\u044b] PASSED [ 53%]
tests.py::TestBooksCollector::test_get_books_genre_genre_for_book[\u0427\u0435\u043b\u043e\u0432\u0435\u043a-\u0430\u043c\u0444\u0438\u0431\u0438\u044f-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 57%]
tests.py::TestBooksCollector::test_get_books_genre_genre_for_book[\u041a\u0440\u0430\u0441\u043d\u0430\u044f \u043b\u0435\u043d\u0442\u0430-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED [ 61%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_specific_genre PASSED                                [ 65%] 
tests.py::TestBooksCollector::test_get_books_genre_viewing_dictionary PASSED                                          [ 69%] 
tests.py::TestBooksCollector::test_get_books_for_children_book_withound_ganre_age_reting[\u0421\u043c\u0435\u0448\u0430\u0440\u0438\u043a\u0438-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED [ 73%]
tests.py::TestBooksCollector::test_get_books_for_children_book_withound_ganre_age_reting[\u0413\u043e\u0440\u0435 \u043e\u0442 \u0443\u043c\u0430-\u041a\u043e\u043c\u0435\u0434\u0438\u0438] PASSED [ 76%]
tests.py::TestBooksCollector::test_get_books_for_children_book_withound_ganre_age_reting[\u0427\u0435\u043b\u043e\u0432\u0435\u043a-\u0430\u043c\u0444\u0438\u0431\u0438\u044f-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 80%]
tests.py::TestBooksCollector::test_get_books_for_children_book_with_ganre_age_reting[\u041f\u0442\u0438\u0446\u044b-\u0423\u0436\u0430\u0441\u044b] PASSED [ 84%]
tests.py::TestBooksCollector::test_get_books_for_children_book_with_ganre_age_reting[\u041a\u0440\u0430\u0441\u043d\u0430\u044f \u043b\u0435\u043d\u0442\u0430-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED [ 88%]
tests.py::TestBooksCollector::test_add_book_in_favorites_book_into_books_genre PASSED                                 [ 92%] 
tests.py::TestBooksCollector::test_delete_book_from_favorites_books_del PASSED                                        [ 96%] 
tests.py::TestBooksCollector::test_list_of_favorites_books_view_list_favorite PASSED                                  [100%] 

==================================================== 26 passed in 0.10s ==================================================== 
