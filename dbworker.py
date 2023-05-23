from vedis import Vedis
import config
import ast

def get_current_state(user_id):
    with Vedis(config.db_state) as db:
        try:
            return db[user_id].decode() # Если используете Vedis версии ниже, чем 0.7.1, то .decode() НЕ НУЖЕН
        except KeyError:  # Если такого ключа почему-то не оказалось
            return config.States.S_FIRST_MESSAGE.value  # значение по умолчанию - начало диалога

# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    with Vedis(config.db_state) as db:
        try:
            db[user_id] = value
            return True
        except:
            return False

def set_previous_message(user_id, previous_message):
    with Vedis(config.db_previous_message) as db:
        try:
            db[user_id] = previous_message
            return True
        except:
            return False

def get_previous_message(user_id):
    with Vedis(config.db_previous_message) as db:
        try:
            return db[user_id].decode() # Если используете Vedis версии ниже, чем 0.7.1, то .decode() НЕ НУЖЕН
        except KeyError:  # Если такого ключа почему-то не оказалось
            return ast.literal_eval({"role": "assistant", "content": "null"})