from interactions import *


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
            footer=EmbedFooter(text="Bot créé par Nephtys, à contacter si besoin.", icon_url=self.bot.user.avatar_url))  
        help.add_field(name="/info", value="Affiche les informations du bot")
        help.add_field(name="/dire", value="Fait parler le bot")
        help.add_field(name="/shifumi", value="Joue au shifumi avec le bot")
        help.add_field(name="/ping", value="Affiche le ping du bot")
        help.add_field(name="/help", value="Affiche toutes les commandes disponibles")
        help.add_field(name="/bagarre", value="C'est l'heure de la bagarre")
        help.add_field(name="/clear", value="Supprime un nombre de messages")
        help.add_field(name="/nick", value="Change le pseudo d'un membre")
        help.add_field(name="/delchannel", value="Supprime un salon")
        help.add_field(name="/delrole", value="Supprime un rôle")
        help.add_field(name="/8ball", value="Pose une question à la boule magique")
        help.add_field(name="/userinfo", value="Affiche les informations d'un utilisateur")
        help.add_field(name="/serveurinfo", value="Affiche les informations du serveur")    
        help.add_field(name=":warning: **Owner-Only** | /reload", value="Recharge les extensions du bot")
        help.Timestamp = Timestamp.now()
        await ctx.send(embed=help)


def setup(bot):
    Help(bot)
