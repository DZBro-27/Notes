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
