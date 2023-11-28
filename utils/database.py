from beanie import *
from interactions import *
import asyncio
from typing import Optional
from decouple import config


from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

from beanie import Document, Indexed, init_beanie
import logging


DB_URL = config("DB_URL")

class Sanctions(BaseModel):
    type : str
    raison :  Optional[str] = None
    user : str
    durée : int

class Server(Document):
    name : str
    id : int
    owner : User
    sanctions : list[Sanctions]

# This is an asynchronous example, so we will access it from an async function
async def example():
    # Beanie uses Motor async client under the hood 
    client = AsyncIOMotorClient(f"{DB_URL}")

    # Initialize beanie with the Product document class
    await init_beanie(database=client.db_name, document_models=[Server])
    logging.info("Base de donné correctement chargée !")
    




if __name__ == "__main__":

    asyncio.run(example())