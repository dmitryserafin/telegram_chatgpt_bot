import telebot
import openai
import config
import dbworker

openai.api_key = config.AI_token
bot=telebot.TeleBot(config.tg_token)
previus_response = {"role": "assistant", "content": "start"}

@bot.message_handler(commands=["image"])
def start_image(message):
  bot.send_message(message.chat.id, "Напиши свою идею для генерации изображения")
  dbworker.set_state(message.chat.id, config.States.S_IMAGE.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_CHAT.value)
def message_chat(message):
    if str(message.chat.id) in config.employees:
        global previus_response
        dbworker.set_state(message.chat.id, config.States.S_CHAT.value)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=512,
            messages=[
                previus_response,
                {"role": "user", "content": message.text}
            ]
        )
        previus_response = completion.choices[0].message
        bot.reply_to(message, completion.choices[0].message.content)
    else:
        bot.reply_to(message, 'Прости, но ты не добавлен в список сотрудников! Обратись к @nickname в slack')

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_IMAGE.value)
def message_image(message):
    if str(message.chat.id) in config.employees:
        completion = openai.Image.create(
            prompt = message.text,
            size="256x256"
        )
        bot.send_photo(message.chat.id, completion.data[0].url)
        bot.send_message(message.chat.id, "отправь /chat если хочешь перейти в режим чата или /image чтобы снова попробовать сгенерировать картинку")
        dbworker.set_state(message.chat.id, config.States.S_CHAT.value)
    else:
        bot.reply_to(message, 'Прости, но ты не добавлен в список сотрудников! Обратись к @nickname в slack')


bot.polling(none_stop=True)

