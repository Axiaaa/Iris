from interactions import *
from const import TOKEN
import logging, os


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
        print(f"{ext} a été chargé !")
        bot.load_extension(f"{folder_name}{ext}")

load_extensions(bot, "ext", "ext.")
load_extensions(bot, "utils", "utils.", ["database.py"])
load_extensions(bot, "moderation", "moderation.")
bot.start()