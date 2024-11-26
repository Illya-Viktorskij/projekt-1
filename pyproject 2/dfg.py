def process_sales_files():
    from calendar import month

    # Список файлів для кожного місяця
    month_files = [
        "month/Jul.", "month/Aug.", "month/Sep.", "month/Oct.",
        "month/Nov.", "month/Dec.", "month/Jan.", "month/Feb.",
        "month/Mar.", "month/Apr.", "month/May.", "month/Jun."
    ]

    # Створюємо порожні файли для кожного місяця
    for file in month_files:
        with open(file, 'w'):
            pass

    # Функція для додавання рядка в файл
    def add_mouth(sale, line_sale):
        with open(sale, 'a') as file:
            file.write(line_sale)

    # Читаємо вхідний файл і розподіляємо рядки по місяцях
    with open("sale", 'r') as file:
        for item in file.readlines():
            if 'Jul.' in item:
                add_mouth(sale='month/Jul.', line_sale=item)
            elif 'Aug.' in item:
                add_mouth(sale='month/Aug.', line_sale=item)
            elif 'Sep.' in item:
                add_mouth(sale='month/Sep.', line_sale=item)
            elif 'Oct.' in item:
                add_mouth(sale='month/Oct.', line_sale=item)
            elif 'Nov.' in item:
                add_mouth(sale='month/Nov.', line_sale=item)
            elif 'Dec.' in item:
                add_mouth(sale='month/Dec.', line_sale=item)
            elif 'Jan.' in item:
                add_mouth(sale='month/Jan.', line_sale=item)
            elif 'Feb.' in item:
                add_mouth(sale='month/Feb.', line_sale=item)
            elif 'Mar.' in item:
                add_mouth(sale='month/Mar.', line_sale=item)
            elif 'Apr.' in item:
                add_mouth(sale='month/Apr.', line_sale=item)
            elif 'May' in item:
                add_mouth(sale='month/May.', line_sale=item)
            elif 'Jun.' in item:
                add_mouth(sale='month/Jun.', line_sale=item)



