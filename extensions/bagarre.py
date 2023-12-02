from interactions import *
from random import randint
import asyncio

class Bagarre(Extension):
    @slash_command(name="bagarre", description="C'est l'heure de la baguarre")
    async def bagarre(self, ctx : InteractionContext):
        """
        C'est l'heure de la baguarre

        Args:
            ctx (InteractionContext): Le contexte

        Returns:
            None
        """
        msg = await ctx.send(content="https://cdn.discordapp.com/attachments/1111756433722187808/1112000937054195732/x.jpg")
        await asyncio.sleep(5)

        choix = randint(0,1)
        if choix == 0:
            await msg.edit(content="https://cdn.discordapp.com/attachments/1111756433722187808/1111998078023630919/l.jpg")
        elif choix == 1:
            await msg.edit(content="https://cdn.discordapp.com/attachments/1111756433722187808/1111998078732484669/w.jpg")


def setup(bot):
    Bagarre(bot)
