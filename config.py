from enum import Enum
import json

with open('variables.json') as variable:
    variables = json.load(variable)

tg_token = variables['tokens']['tg_token']
AI_token = variables['tokens']['AI_token']
employees = variables['employees']
db_file = "database.vdb"

class States(Enum):

    S_IMAGE = "0"  # стейт генерации картинок
    S_CHAT = "1" # стейт чата