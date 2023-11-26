from interactions import *
import logging

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

def setup(bot):
    Listen(bot)