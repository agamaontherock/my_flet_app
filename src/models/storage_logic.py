import json
import os

STORAGE_DIR = "storage"
FILE_PATH = os.path.join(STORAGE_DIR, "user_data.json")

def load_user_data() -> dict:
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            print("Помилка при завантаженні даних.")
    return {"username": "Гість"}

def save_user_data(data: dict):
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)