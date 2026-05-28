def validate_username(new_name):
    name = new_name.strip()
    if not name:
        return False, "Ім'я не може бути порожнім."
    if len(name) < 3:
        return False, "Ім'я занадто коротке (мін. 3 символи)."
    return True, "Дані успішно перевірено!"