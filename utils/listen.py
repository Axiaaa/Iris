from interactions import *
import logging
from utils.db_cmds import DB_commands

class Listen(Extension) : 

    @listen(event_name=events.Startup)
    async def on_startup(self, ctx : InteractionContext):
        logging.info("Iris est prêt !")

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
    async def on_guild_join(self, event: events.GuildJoin):
        await DB_commands.get_serv_info(event)


    @listen(event_name=events.GuildUpdate)
    async def on_guild_update(self, event: events.GuildUpdate):
        await DB_commands.update_serv_info(event)

    @listen(event_name=events.Error)
    async def on_error(self, event : events.Error):
        await self.bot.get_channel(1182411280015949954).send(f"Hey <@240430740158939139>, une erreur est survenue : {event.source} -> {event.error}")

def setup(bot):
    Listen(bot)