from interactions import Extension, InteractionContext, Member, events
from motor.motor_asyncio import AsyncIOMotorClient
from utils.db import Server, Sanctions, Ticket, DB_User, DB_Roles
from beanie import PydanticObjectId
from beanie import init_beanie
from const import DB_URL
import logging
import datetime

class DB_commands(Extension):
    def __init__(self, client):
        self.client = client

    async def add_sanction(self, ctx: InteractionContext, sanction_type: str, reason: str, target_user: Member):
        serv = await Server.find_one(Server.srv_id == str(ctx.guild.id))
        if serv:
            serv.sanctions.append(
                Sanctions(
                    id=PydanticObjectId(),
                    user_id=str(target_user.id),
                    user_name=target_user.username,
                    reason=reason,
                    mod_id=str(ctx.author.id),
                    mod_name=ctx.author.username,
                    s_type=sanction_type,
                    date=datetime.datetime.utcnow()
                )
            )
            await serv.save()
            logging.info(f"{target_user.username} a reçu une sanction de type {sanction_type} dans le serveur {ctx.guild.name}.")

    async def get_warn_count(self, ctx: InteractionContext, user_id: str):
        serv = await Server.find_one(Server.srv_id == str(ctx.guild.id))
        if serv:
            return sum(1 for sanction in serv.sanctions if sanction.user_id == user_id and sanction.s_type == "warn")
        return 0
    @staticmethod
    async def create_ticket(ctx: InteractionContext, ticket_channel):
        serv = await Server.find_one(Server.srv_id == str(ctx.guild.id))
        if serv:
            serv.tickets.append(
                Ticket(
                    ticket_id=str(ticket_channel.id),
                    ticket_user=f"{ctx.author.username} | {ctx.author.id}",
                    ticket_status="open",
                    allowed_users=[str(ctx.author.id)]
                )
            )
            await serv.save()
            logging.info(f"Ticket {ticket_channel.name} créé par {ctx.author.username} dans le serveur {ctx.guild.name}.")

    @staticmethod
    async def change_ticket_status(ctx: InteractionContext, ticket_id: str, status: str):
        serv = await Server.find_one(Server.srv_id == str(ctx.guild.id))
        if serv:
            for ticket in serv.tickets:
                if ticket.ticket_id == ticket_id:
                    ticket.ticket_status = status
            await serv.save()
            logging.info(f"Statut du ticket {ticket_id} changé en {status} dans le serveur {ctx.guild.name}.")

    @staticmethod
    async def delete_ticket(ctx: InteractionContext, ticket_id: str):
        serv = await Server.find_one(Server.srv_id == str(ctx.guild.id))
        if serv:
            serv.tickets = [ticket for ticket in serv.tickets if ticket.ticket_id != ticket_id]
            await serv.save()
            logging.info(f"Ticket {ticket_id} supprimé du serveur {ctx.guild.name}.")

    @staticmethod
    async def check_ticket(ctx: InteractionContext, user_id: str):
        serv = await Server.find_one(Server.srv_id == str(ctx.guild.id))
        if serv:
            return any(ticket.ticket_user == user_id and ticket.ticket_status == "open" for ticket in serv.tickets)
        return False

    @staticmethod
    async def get_serv_info(event: events.GuildJoin):
        client = AsyncIOMotorClient(DB_URL)
        await init_beanie(database=client.db_name, document_models=[Server])
        serv = await Server.find_one(Server.srv_id == str(event.guild.id))
        if not serv:
            new_serv = Server(
                srv_id=str(event.guild.id),
                name=event.guild.name,
                owner_id=str(event.guild.get_owner().id),
                member_count=event.guild.member_count,
                sanctions=[],
                tickets=[]
            )
            for role in event.guild.roles :
                new_serv.role.append(
                    DB_Roles(
                        role_id = f"{role.id}",
                        role_name = f"{role.name}",
                        role_perms = str(role.permissions).split('|')
                    )
                )
            for user in event.guild.members :
                if not user.bot :
                    new_serv.user.append(
                        DB_User(
                            user_id = f"{user.id}",
                            user_name = f"{user.global_name}",
                            user_perms = str(user.guild_permissions).split('|'),
                            user_roles = [f"{role.name} {role.id}" for role in user.roles]
                        )
                )
            await new_serv.insert()
            logging.info(f"Serveur {event.guild.name} ajouté à la base de données.")

    @staticmethod
    async def update_serv_info(event: events.GuildUpdate):
        serv = await Server.find_one(Server.srv_id == str(event.after.id))
        if serv:
            serv.name = event.after.name
            serv.owner_id = str(event.after.get_owner().id)
            serv.member_count = event.after.member_count
            for role in event.after.roles :
                serv.role.append(
                    DB_Roles(
                        role_id = f"{role.id}",
                        role_name = f"{role.name}",
                        role_perms = str(role.permissions).split('|')
                    )
                )
                for user in event.after.members :
                    if not user.bot :
                        serv.user.append(
                            DB_User(
                                user_id = f"{user.id}",
                                user_name = f"{user.global_name}",
                                user_perms = str(user.guild_permissions).split('|'),
                                user_roles = [f"{role.name} {role.id}" for role in user.roles]
                            )
                    )
            await serv.save()
            logging.info(f"Serveur {event.after.name} mis à jour dans la base de données.")

def setup(bot):
    DB_commands(bot)
