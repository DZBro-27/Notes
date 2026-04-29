import os
import re


def build_note(note_text, note_name):
    try:
        with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
            file.write(note_text)
        print(f"Заметка {note_name} создана!")
    except OSError as e:
        print(f"Ошибка при работе с файлом: {e}")


def create_note():
    """Создает файл с заметкой"""

    forbidden_symbols = "\\|/*<>?:"

    while True:
        note_name = input("Введите название заметки: ").strip()

        if not note_name:
            print("Название не может быть пустым.")

        elif any(symbol in note_name for symbol in forbidden_symbols):
            print("Недопустимые символы в названии. Попробуйте снова!")

        else:
            break

    note_text = input("Введите текст заметки: ")

    build_note(note_text, note_name)


def read_note():
    """Читает и выводит заметку"""

    try:
        note_name_read = input(
            "Введите название заметки, которую хотите прочитать: "
        ).strip()
        path = f"{note_name_read}.txt"

        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as file:
                note_text = file.read()
            print(note_text)

        else:
            print("Заметка с таким названием не существует")

    except OSError as e:
        print(f"Ошибка при работе с файлом: {e}")


def edit_note():
    """Редактирует заметку"""

    try:
        note_name_edit = input(
            "Введите название заметки, которую хотите отредактировать: "
        ).strip()
        path = f"{note_name_edit}.txt"

        if os.path.isfile(path):
            print("Такая заметка существует!")
            edit_note_text = input("Введите новый текст заметки: ")

            with open(path, "w", encoding="utf-8") as file:
                file.write(edit_note_text)
            print(f"Заметка {note_name_edit} отредактирована!")

        else:
            print("Заметка с таким названием не существует")

    except OSError as e:
        print(f"Ошибка при работе с файлом: {e}")


def delete_note():
    """Удаляет заметку."""

    try:

        trash_note = input("Введите имя заметки, которую хотите удалить:").strip()
        path = f"{trash_note}.txt"

        if os.path.isfile(path):
            os.remove(path)
            print(f"Заметка {trash_note} удалена!")

        else:
            print(f"Заметка с именем {trash_note} не найдена.")

    except OSError as e:
        print(f"Ошибка при работе с файлом: {e}")


def display_notes():
    """Выводит все заметки от самой короткой к самой длинной."""

    try:
        notes = []

        for note in os.listdir():
            if note.endswith(".txt"):
                notes.append(note)

        sorted_notes = sorted(notes, key=len)

        if sorted_notes:
            print("Заметки от самой короткой к самой длинной:")

            for note in sorted_notes:
                print(note)
        else:
            print("Заметок пока нет.")

    except OSError as e:
        print(f"Ошибка при работе с файлами: {e}")


def display_sorted_notes():
    """Выводит все заметки от самой длинной к самой короткой."""

    try:
        notes = []

        for note in os.listdir():
            if note.endswith(".txt"):
                notes.append(note)

        sorted_notes = sorted(notes, key=len, reverse=True)

        if sorted_notes:
            print("Заметки от самой длинной к самой короткой:")

            for note in sorted_notes:
                print(note)
        else:
            print("Заметок пока нет.")

    except OSError as e:
        print(f"Ошибка при работе с файлами: {e}")
