from enum import Enum

tg_token = '<your_Telegram_token>'
AI_token = '<your_OpenAi_token>'
db_file = "database.vdb"

class States(Enum):

    S_IMAGE = "0"  # стейт генерации картинок
    S_CHAT = "1" # стейт чата