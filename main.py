# Задача 5.1.1
genres = ("Роман", "Новелла", "Фэнтези", "Научная Фантастика")
numbers = (3, 7, 9, 1, 6, 8, 2, 5, 4)


length_genres = len(genres)
length_numbers = len(numbers)


max_number = max(numbers)
min_number = min(numbers)
sum_numbers = sum(numbers)

sorted_numbers_asc = tuple(sorted(numbers))
sorted_numbers_desc = tuple(sorted(numbers, reverse=True))

print("Длина кортежа жанров:", length_genres)
print("Длина кортежа чисел:", length_numbers)
print("Максимальный элемент в кортеже чисел:", max_number)
print("Минимальный элемент в кортеже чисел:", min_number)
print("Сумма всех элементов в кортеже чисел:", sum_numbers)
print("Отсортированные числа по возрастанию:", sorted_numbers_asc)
print("Отсортированные числа по убыванию:", sorted_numbers_desc)

# Задача 5.1.2

cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")
updated_genres = tuple("Боевик" if genre == "Экшн" else genre for genre in cinema_genres)
updated_genres = updated_genres[:2] + ("Фэнтези",) + updated_genres[2:]

print(updated_genres)

genres_string = ", ".join(updated_genres)

print(f"Обновленные жанры кино: {genres_string}")

# Задача 5.1.3

my_items = {"нож", "спички", "палатка", "фонарь", "веревка", "аптечка", "топор", "карта", "спальник", "компас"}
friend_items = {"нож", "спички", "палатка", "удочка", "спальник", "бинокль", "солнечные батареи", "карта", "топор", "рация"}


all_items = my_items | friend_items
print("Вещи, которые взяли бы вы двое:", all_items)


only_my_items = my_items - friend_items
print("Вещи, которые взяли бы только вы:", only_my_items)


only_friend_items = friend_items - my_items
print("Вещи, которые взял бы только ваш близкий человек:", only_friend_items)


common_items = my_items & friend_items
print("Вещи, которые есть у вас обоих:", common_items)

# Задача 5.1.4

import random

cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]
genres_set = set(cinema_genres)
genres_set.add("драма")
genres_set.add("фантастика")
genres_set.remove("триллер")


genres_set.pop()  # удаляет  элем

final_genres_list = list(genres_set)

print(final_genres_list)
