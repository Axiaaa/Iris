from interactions import *


class Ping(Extension):

    @slash_command(name="ping", description="Ping le bot")
    async def command_ping(self, ctx: InteractionContext):
        """
        Ping le bot

        Args:
            ctx (InteractionContext): Le contexte

        Returns:
            None
        """
        try : 
            websocket = self.bot.latency * 100
            await ctx.send(f"Pong ! :ping_pong: {round(websocket)} ms", ephemeral=True)
        except OverflowError: 
            await ctx.send("Le bot démarre... Attendez une dizaine de secondes puis recommencer :)", ephemeral=True)

def setup(bot):
    Ping(bot)
    