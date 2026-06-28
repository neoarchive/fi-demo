
from fastapi_interactions import Bot
from commands import router
from environs import env
import sys

env.read_env()

vercel_env = env.str('VERCEL_ENV')

if vercel_env and vercel_env != "production":
    print(f"Skipping command sync: VERCEL_ENV={vercel_env!r}")
    sys.exit(0)

app_id = env.int('DISCORD_APP_ID')
public_key = env.str('DISCORD_APP_ID')
bot_token = env.str('DISCORD_BOT_TOKEN')

bot = Bot(
    app_id=app_id,
    public_key=public_key,
    bot_token=bot_token
)

bot.attach_router(router)
bot.sync_commands()
print("Commands synced successfully!")