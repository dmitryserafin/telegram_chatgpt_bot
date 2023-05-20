This project is a Telegram bot that can generate text responses and images upon user request.

To start using the bot, simply send a message with your query to the bot's chat. If you want to request an image generation, use the /image command and the bot will prompt you to enter your idea for image generation.

The bot is based on the open API OpenAI and uses GPT-3 for text generation and DALL-E for image generation.

Additionally, the bot has a chat mode that can be activated with the /chat command. In chat mode, you can have a conversation with the bot and get answers to your questions.

To use the bot, you need to specify the tokens for OpenAI API and Telegram in the config.py file.

This project can be used as a basis for developing other bots and integrations with OpenAI API.

Installation:
- Clone or download the project from the repository
- Install the required dependencies by running the following command in your terminal: `python -m pip install -r requirements.txt`

Usage:
- Before running the bot, make sure to specify your tokens for OpenAI API and Telegram in the `config.py` file
- To start the bot, run the `main.py` file in your terminal
- Send a message to the bot's chat with your query to get a text or image response
- If you want to request an image generation, use the `/image` command and enter your idea for image generation when prompted
- To activate chat mode, use the `/chat` command
- To stop the bot, press Ctrl + C in your terminal

