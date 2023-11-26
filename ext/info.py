from interactions import *

class Info(Extension):

    @slash_command(name="info", description="Affiche les informations du bot")
    async def info(self, ctx : InteractionContext):
            """
            Affiche les informations du bot

            Args:
                ctx (InteractionContext): Le contexte
            
            Returns:
                None
            """
            try : 
                embed = Embed(title="Informations du bot", color=Color.from_hex("#FF0000"), timestamp=Timestamp.now())
                embed.add_field(name="Développé en", value="Python, avec [interactions.py (v5)](https://github.com/interactions-py/interactions.py)", inline=True)
                embed.add_field(name="Créé le", value=f"<t:1685136462:F>", inline=False)
                embed.add_field(name="Créé par", value=self.bot.owner, inline=False)
                embed.add_field(name="Serveurs", value=len(self.bot.guilds), inline=True)
                embed.add_field(name="Latence", value=f"{round(self.bot.latency * 100)} ms", inline=True)
                # embed.add_field("Pour m'inviter sur votre serveur", value = "Cliquez **[ici](https://discord.com/api/oauth2/authorize?client_id=1111756058902409327&permissions=8&scope=bot)**")
                await ctx.send(embed=embed)
            except OverflowError : 
                await ctx.send("La commande est indisponible pour le moment. Réessayes dans quelques minutes.", ephemeral=True)


def setup(bot):
    Info(bot)
