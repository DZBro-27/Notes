import os
import re


def build_note(note_text, note_name):
    try:
        with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
            file.write(note_text)
        print(f"Заметка {note_name} создана!")
    except OSError as e:
        print(f"Ошибка при работе с файлом: {e}")