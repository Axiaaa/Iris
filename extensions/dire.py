from interactions import *
import logging

class Dire(Extension):
    @slash_command(name="dire", description="Fais parler le bot")
    @slash_option(name="texte", description="Ce que le bot doit dire", opt_type=OptionType.STRING)
    async def dire(self,ctx: InteractionContext, texte : str):
        """
        Fais parler le bot

        Args:
            ctx (InteractionContext): Le contexte
            texte (str): Ce que le bot doit dire

        Returns:
            None
        """ 
        await ctx.send("Message envoyé :white_check_mark:", ephemeral=True)
        logging.info(f"{ctx.author.username} ({ctx.author_id}) a utilisé /dire pour envoyer : {texte}")
        await ctx.channel.send(texte)

def setup(bot):
    Dire(bot)
    