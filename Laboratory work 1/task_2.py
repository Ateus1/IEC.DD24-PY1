# TODO Найдите количество книг, которое можно разместить на дискете
volume_of_diskette_mb = 1.44
count_of_pages = 100
count_of_strings = 50
count_of_symbols = 25
volume_of_symbol_b = 4

volume_of_diskette_b = volume_of_diskette_mb * 1024 * 1024
volume_of_book_b = count_of_pages * count_of_strings * count_of_symbols * volume_of_symbol_b
count_of_books = int(volume_of_diskette_b//volume_of_book_b)
print("Количество книг, помещающихся на дискету:", count_of_books)
