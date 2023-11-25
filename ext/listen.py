from interactions import *
import logging

class Listen(Extension) : 

    @listen(event_name=events.Startup)
    async def on_startup(self, ctx : InteractionContext):
        await self.bot.change_presence(
        status=Status.ONLINE,
        activity=Activity(name="You 👀",
                          type=ActivityType.WATCHING
                        )
    )
        logging.info("bot_sans_nom est prêt !")

def setup(bot):
    Listen(bot)