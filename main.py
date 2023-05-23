import telebot
import openai
import config
import dbworker
import ast

openai.api_key = config.AI_token
bot=telebot.TeleBot(config.tg_token)

@bot.message_handler(commands=["image"])
def start_image(message):
  bot.send_message(message.chat.id, "Напиши свою идею для генерации изображения")
  dbworker.set_state(message.chat.id, config.States.S_IMAGE.value)

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Пиши произвольный запрос для начала работы")
    dbworker.set_state(message.chat.id, config.States.S_FIRST_MESSAGE.value)

@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Контекст обнулен. Пиши произвольный запрос для начала работы")
    dbworker.set_state(message.chat.id, config.States.S_FIRST_MESSAGE.value)
    dbworker.set_previous_message(message.chat.id, {"role": "assistant", "content": "null"})

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_FIRST_MESSAGE.value)
def first_mesage(message):
    if str(message.chat.id) in config.employees:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=config.max_tokens,
            messages=[
                {"role": "user", "content": message.text}
            ]
        )
        bot.reply_to(message, completion.choices[0].message.content)
        dbworker.set_previous_message(message.chat.id, completion.choices[0].message)
        dbworker.set_state(message.chat.id, config.States.S_SECOND_MESSAGE.value)
    else:
        bot.reply_to(message, 'Прости, но ты не добавлен в список сотрудников! Обратись к @nickname в slack')

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SECOND_MESSAGE.value)
def second_mesage(message):
    if str(message.chat.id) in config.employees:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=config.max_tokens,
            messages=[
                ast.literal_eval(dbworker.get_previous_message(message.chat.id)),
                {"role": "user", "content": message.text}
            ]
        )
        bot.reply_to(message, completion.choices[0].message.content)
        dbworker.set_previous_message(message.chat.id, completion.choices[0].message)
        dbworker.set_state(message.chat.id, config.States.S_SECOND_MESSAGE.value)
    else:
        bot.reply_to(message, 'Прости, но ты не добавлен в список сотрудников! Обратись к @nickname в slack')

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_IMAGE.value)
def message_image(message):
    if str(message.chat.id) in config.employees:
        completion = openai.Image.create(
            prompt = message.text,
            size=config.image_size
        )
        bot.send_photo(message.chat.id, completion.data[0].url)
        bot.send_message(message.chat.id, "отправь /image чтобы снова попробовать сгенерировать картинку")
        dbworker.set_state(message.chat.id, config.States.S_FIRST_MESSAGE.value)
    else:
        bot.reply_to(message, 'Прости, но ты не добавлен в список сотрудников! Обратись к @nickname в slack')


bot.polling(none_stop=True)

