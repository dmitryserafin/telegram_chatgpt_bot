import telebot
import openai
import config
import dbworker

openai.api_key = config.AI_token
bot=telebot.TeleBot(config.tg_token)
previus_response = 'null'

@bot.message_handler(commands=["image"])
def start_image(message):
  bot.send_message(message.chat.id, "Напиши свою идею для генерации изображения")
  dbworker.set_state(message.chat.id, config.States.S_IMAGE.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_CHAT.value)
def message_chat(message):
  global previus_response
  dbworker.set_state(message.chat.id, config.States.S_CHAT.value)
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens = 512,
    messages=[
      {"role": "assistant", "content": previus_response},
      {"role": "user", "content": message.text}
    ]
)
  previus_response = completion.choices[0].message.content
  bot.reply_to(message, completion.choices[0].message.content)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_IMAGE.value)
def message_image(message):
  completion = openai.Image.create(
    prompt = message.text,
    size="256x256"
  )
  bot.send_photo(message.chat.id, completion.data[0].url)
  bot.send_message(message.chat.id, "отправь /chat если хочешь перейти в режим чата или /image чтобы снова попробовать сгенерировать картинку")
  dbworker.set_state(message.chat.id, config.States.S_CHAT.value)


bot.polling(none_stop=True)

