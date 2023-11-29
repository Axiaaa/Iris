from beanie import *
from interactions import *
from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from beanie import Document, init_beanie
import logging


class Sanctions(BaseModel):
    user_id : str
    user_name : str
    reason : str
    mod_id : str
    mod_name : str
    s_type : str
    date : str

class Server(Document):
    srv_id : str
    name : str
    owner_id : int
    owner_name : str
    sanctions : list[Sanctions] = []
    
DB_URL = config("DB_URL")


async def get_serv_info(event: events.GuildJoin):
    client = AsyncIOMotorClient(f"{DB_URL}")
    await init_beanie(database=client.db_name, document_models=[Server])
    srv_id = event.guild.id
    serv = await Server.find_one(Server.srv_id == f"{srv_id}")
    if serv is None:
        serv = Server(
            srv_id = f"{event.guild.id}",
            name = event.guild.name,
            owner_id = event.guild.get_owner().id,
            owner_name = event.guild.get_owner().global_name
        )
        await serv.insert()
        logging.info(f"Serveur {event.guild.name} ajouté à la base de donnée !")
    else:
        logging.info(f"Serveur {event.guild.name} déjà présent dans la base de donnée !")
