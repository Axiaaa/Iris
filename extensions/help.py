from interactions import *
from const import BOT_VERSION

class Help(Extension):
    
    @slash_command(name="help", description="Affiche toutes les commandes disponibles")
    async def help(self, ctx : InteractionContext):
        """
        Affiche toutes les commandes disponibles

        Args:
            ctx (InteractionContext): Le contexte

        Returns:
            None
        """
        help = Embed(
            title="Voici la liste de toutes les commandes disponibles",
            footer=EmbedFooter(text=f"Version du bot {BOT_VERSION}", icon_url=self.bot.user.avatar_url))  
        help.add_field(name="/info", value="Affiche les informations du bot")
        help.add_field(name="/dire", value="Fait parler le bot")
        help.add_field(name="/shifumi", value="Joue au shifumi avec le bot")
        help.add_field(name="/ping", value="Affiche le ping du bot")
        help.add_field(name="/help", value="Affiche toutes les commandes disponibles")
        help.add_field(name="/bagarre", value="C'est l'heure de la bagarre")
        help.add_field(name="/8ball", value="Pose une question à la boule magique")
        help.add_field(name="/userinfo", value="Affiche les informations d'un utilisateur")
        help.add_field(name="/serveurinfo", value="Affiche les informations du serveur")
        help.add_field(name="/action_ou_verite", value="Joue à Action ou Vérité")
        help.add_field(name="/roll", value="Lance un dé à six faces")
        help.color = Color.from_hex("#2596be")
        help.Timestamp = Timestamp.now()
        await ctx.send(embed=help)


def setup(bot):
    Help(bot)
