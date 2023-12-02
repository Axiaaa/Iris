from beanie import *
from interactions import *
from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from beanie import Document, init_beanie
import logging


class Sanctions(BaseModel):
    id : PydanticObjectId()
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
