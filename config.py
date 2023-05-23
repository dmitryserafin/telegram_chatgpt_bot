from enum import Enum
import json

with open('variables.json') as variable:
    variables = json.load(variable)

tg_token = variables['tokens']['tg_token']
AI_token = variables['tokens']['AI_token']
employees = variables['employees']
db_state = "database_state.vdb"
db_previous_message = "database_previous_message.vdb"
max_tokens = 1024
image_size = "256x256"

class States(Enum):

    S_IMAGE = "0"  # стейт генерации картинок
    S_FIRST_MESSAGE = "1" # стейт первого сообщения в чате
    S_SECOND_MESSAGE = "2"  # стейт второго сообщения в чате с контекстом первого