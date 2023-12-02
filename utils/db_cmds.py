from interactions import *
from beanie import *
from interactions import *
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import logging
from const import DB_URL
from utils.db import Server, Sanctions
import datetime

class DB_commands(Extension) :

    async def DB_add_ban(ctx : InteractionContext, reason : str, target_user : Member):
        client = AsyncIOMotorClient(f"{DB_URL}")
        await init_beanie(database=client.db_name, document_models=[Server])
        serv = await Server.find_one(Server.srv_id == f"{ctx.guild.id}")
        serv.sanctions.append(
            Sanctions(
                id = PydanticObjectId(),
                user_id = f"{target_user.id}",
                user_name = f"{target_user.global_name}",
                reason = f"{reason}",
                mod_id = f"{ctx.author.id}",
                mod_name = f"{ctx.author.global_name}",
                s_type = "ban",
                date = f"{datetime.datetime.utcnow()}"
            )
        )
        await serv.save()
        logging.info(f"{target_user.global_name} a été banni du serveur {ctx.guild.name} !")

    
    async def DB_add_kick(ctx : InteractionContext, reason : str, target_user : Member):
        client = AsyncIOMotorClient(f"{DB_URL}")
        await init_beanie(database=client.db_name, document_models=[Server])
        serv = await Server.find_one(Server.srv_id == f"{ctx.guild.id}")
        serv.sanctions.append(
            Sanctions(
                id = PydanticObjectId(),
                user_id = f"{target_user.id}",
                user_name = f"{target_user.global_name}",
                reason = f"{reason}",
                mod_id = f"{ctx.author.id}",
                mod_name = f"{ctx.author.global_name}",
                s_type = "kick",
                date = f"{datetime.datetime.utcnow()}"
            )
        )
        await serv.save()
        logging.info(f"{target_user.global_name} a été kick du serveur {ctx.guild.name} !")

    async def DB_add_mute(ctx : InteractionContext, duree : str, reason : str, target_user : Member):
        client = AsyncIOMotorClient(f"{DB_URL}")
        await init_beanie(database=client.db_name, document_models=[Server])
        serv = await Server.find_one(Server.srv_id == f"{ctx.guild.id}")
        serv.sanctions.append(
            Sanctions(
                id = PydanticObjectId(),
                user_id = f"{target_user.id}",
                user_name = f"{target_user.global_name}",
                reason = f"{reason}\nDurée : {duree}",
                mod_id = f"{ctx.author.id}",
                mod_name = f"{ctx.author.global_name}",
                s_type = "mute",
                date = f"{datetime.datetime.utcnow()}"
            )
        )
        await serv.save()
        logging.info(f"{target_user.global_name} a été mute du serveur {ctx.guild.name} !")

    async def DB_add_warn(ctx : InteractionContext, reason : str, target_user : Member):
        client = AsyncIOMotorClient(f"{DB_URL}")
        await init_beanie(database=client.db_name, document_models=[Server])
        serv = await Server.find_one(Server.srv_id == f"{ctx.guild.id}")
        serv.sanctions.append(
            Sanctions(
                id = PydanticObjectId(),
                user_id = f"{target_user.id}",
                user_name = f"{target_user.global_name}",
                reason = f"{reason}",
                mod_id = f"{ctx.author.id}",
                mod_name = f"{ctx.author.global_name}",
                s_type = "warn",
                date = f"{datetime.datetime.utcnow()}"
            )
        )
        await serv.save()
        logging.info(f"{target_user.global_name} a été warn du serveur {ctx.guild.name} !")

        
    async def DB_add_unban(ctx : InteractionContext, reason : str, target_user : Member):
        client = AsyncIOMotorClient(f"{DB_URL}")
        await init_beanie(database=client.db_name, document_models=[Server])
        serv = await Server.find_one(Server.srv_id == f"{ctx.guild.id}")
        serv.sanctions.append(
            Sanctions(
                id = PydanticObjectId(),
                user_id = f"{target_user.id}",
                user_name = f"{target_user.global_name}",
                reason = f"{reason}",
                mod_id = f"{ctx.author.id}",
                mod_name = f"{ctx.author.global_name}",
                s_type = "unban",
                date = f"{datetime.datetime.utcnow()}"
            )
        )
        await serv.save()
        logging.info(f"{target_user.global_name} a été débanni du serveur {ctx.guild.name} !")
    
    async def DB_add_unmute(ctx : InteractionContext, reason : str, target_user : Member):
        client = AsyncIOMotorClient(f"{DB_URL}")
        await init_beanie(database=client.db_name, document_models=[Server])
        serv = await Server.find_one(Server.srv_id == f"{ctx.guild.id}")
        serv.sanctions.append(
            Sanctions(
                id = PydanticObjectId(),
                user_id = f"{target_user.id}",
                user_name = f"{target_user.global_name}",
                reason = f"{reason}",
                mod_id = f"{ctx.author.id}",
                mod_name = f"{ctx.author.global_name}",
                s_type = "unmute",
                date = f"{datetime.datetime.utcnow()}"
            )
        )
        await serv.save()
        logging.info(f"{target_user.global_name} a été unmute du serveur {ctx.guild.name} !")
    
    async def DB_get_logs(ctx : InteractionContext, target_user : Member, embed : Embed):
        client = AsyncIOMotorClient(f"{DB_URL}")
        await init_beanie(database=client.db_name, document_models=[Server])
        serv = await Server.find_one(Server.srv_id == f"{ctx.guild.id}")
        logs = serv.sanctions
        logs.reverse()
        for log in logs :
            if log.user_id == f"{target_user.id}" :
                embed.add_field(
                    name=f"{log.s_type.upper()}",
                    value=f"Raison : {log.reason}\nModérateur : <@{log.mod_id}>\nDate : {log.date[:19]}\nID : ||{log.id}||",
                    inline=False
                )
        return embed
    
    async def DB_del_sanction(ctx : InteractionContext, sanction_id : PydanticObjectId):
        client = AsyncIOMotorClient(f"{DB_URL}")
        await init_beanie(database=client.db_name, document_models=[Server])
        serv = await Server.find_one(Server.srv_id == f"{ctx.guild.id}")
        logs = serv.sanctions
        for log in logs :
            if log.id == sanction_id :
                serv.sanctions.remove(log)
        await serv.save()
        logging.info(f"Sanction {sanction_id} supprimée !")

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


def setup(bot):
    DB_commands(bot)
