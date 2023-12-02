from interactions import *
from const import TOKEN, DB_URL
import logging, os, asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from utils.db import Server

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%H:%M:%S",
                    handlers=[
                        logging.FileHandler("bot.log"),
                        logging.StreamHandler()
                    ])

bot = Client(token=TOKEN, intents=Intents.ALL);

def load_extensions(bot, folder, folder_name="", exclude_files=[]):
    extensions = [file.replace(".py", "") for file in os.listdir(folder) if file.endswith(".py") and file not in exclude_files]
    for ext in extensions:
        logging.debug(f"{ext} a été chargé !")
        bot.load_extension(f"{folder_name}{ext}")

load_extensions(bot, "extensions", "extensions.")
load_extensions(bot, "utils", "utils.", exclude_files=["db.py"])
load_extensions(bot, "moderation", "moderation.")

async def init_db():
    client = AsyncIOMotorClient(f"{DB_URL}")
    await init_beanie(database=client.db_name, document_models=[Server])
    logging.info("Connexion à la base de données réussie !")

asyncio.run(init_db())
bot.start()