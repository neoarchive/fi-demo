from fastapi_interactions import Bot
from commands import router
from environs import env 

env.read_env()

app_id = env.int('DISCORD_APP_ID')
public_key = env.str('DISCORD_PUBLIC_KEY')
bot_token = env.str('DISCORD_BOT_TOKEN')

bot = Bot(
    app_id=app_id,
    public_key=public_key,
    bot_token=bot_token
)

bot.attach_router(router)

app = bot.app
