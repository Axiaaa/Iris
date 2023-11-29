from interactions import *
from beanie import *
from interactions import *
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import logging
from const import DB_URL
from pydantic import BaseModel
from utils.db import Server, Sanctions

class DB_commands(Extension) :

    async def DB_add_ban(ctx : InteractionContext, reason : str, target_user : Member):
        client = AsyncIOMotorClient(f"{DB_URL}")
        await init_beanie(database=client.db_name, document_models=[Server])
        serv = await Server.find_one(Server.srv_id == f"{ctx.guild.id}")
        serv.sanctions.append(
            Sanctions(
                user_id = f"{target_user.id}",
                user_name = f"{target_user.global_name}",
                reason = f"{reason}",
                mod_id = f"{ctx.author.id}",
                mod_name = f"{ctx.author.global_name}",
                s_type = "ban",
                date = f"{Timestamp.now()}"
            )
        )
        await serv.save()
        logging.info(f"{target_user.global_name} a été banni du serveur {ctx.guild.name} !")

def setup(bot):
    DB_commands(bot)
