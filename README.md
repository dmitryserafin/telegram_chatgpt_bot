# Project Readme

This project provides companies with a way to give their employees access to ChatGPT through Telegram. The project uses OpenAI tokens and a list of employees stored in a `variables.json` file.

## Installation

1. Clone this repository
2. Install the required packages by running `pip install -r requirements.txt`
3. Create a `variables.json` file with the following structure:

```
{
  "tokens": {
    "tg_token": "telegram_bot_token",
    "AI_token": "openai_token"
  },
  "employees": [
    "telegram_chat_id"
  ]
}
```

4. Replace `telegram_bot_token` and `openai_token` with your own Telegram bot token and OpenAI token respectively.
5. Add the Telegram chat IDs of all employees who should have access to the bot.

## Usage

To get started, run the following command:

```
python main.py
```

### How to Get Chat ID

To get your chat ID, follow these steps:

1. Start a conversation with `@getmyid_bot` in Telegram.
2. Send the `/start` command to `@getmyid_bot`.
3. The bot will respond with your chat ID.

### Available Commands

- `/image` - Start a conversation to generate an image
- `/chat` - Start a conversation with ChatGPT

## Authors

- Dmitry Serafin

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
