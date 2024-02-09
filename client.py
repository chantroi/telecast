from hydrogram import Client
from init import api_id, api_hash, bot_token
from app import app

bot = Client("Bot", api_id, api_hash, bot_token=bot_token, plugins=dict(root="commands"), in_memory=True)
app.start()
bot.run()