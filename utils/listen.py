from interactions import *
import logging
from beanie import Document
from database import Sanctions, Optional

class Listen(Extension) : 

    @listen(event_name=events.Startup)
    async def on_startup(self, ctx : InteractionContext):
        logging.info("bot_sans_nom est prêt !")

    @listen(disable_default_listeners=True)
    async def on_command_error(self, event : errors.CommandOnCooldown):
        if isinstance(event.error, errors.CommandOnCooldown):
            await event.ctx.send(
                f"Cette commande est sous cooldown ! Réessaye dans {round(event.error.cooldown.get_cooldown_time())} secondes",
                ephemeral=True,
            )
        else:
            await self.bot.on_command_error(self.bot, event)

    @listen(event_name=events.MessageCreate)
    async def on_message(self, event : events.MessageCreate):
        if self.bot.user.mention in event.message.content:
            await event.message.reply("Salut ! Je vois que tu as essayé de me ping, mon préfix est `/` ! Pour plus d'informations, fais `/help`")


    @listen(event_name=events.GuildJoin)
    async def on_guild_join(self, event : events.GuildJoin):
        class Server(Document):
            name : str
            id : int
            owner : Member
            sanctions : Optional[list[Sanctions]] = None
        
        server = await Server(name=event.guild.name, id=event.guild.id, owner=event.guild.get_owner())
        await server.insert()
        
def setup(bot):
    Listen(bot)