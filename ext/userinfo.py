from interactions import *
import datetime


class Userinfo(Extension):

    @slash_command(name="userinfo", description="Affiche les informations d'un utilisateur")
    @slash_option(name="user", description="L'utilisateur dont vous voulez voir les informations", opt_type=OptionType.USER )
    async def userinfo(self, ctx : InteractionContext, user : Member     = None):
        """
        Affiche les informations d'un utilisateur

        Args:
            ctx (InteractionContext): Le contexte
            user (Member, optional): L'utilisateur. Defaults to None.
        
        Returns:
            None
        """

        if user is None:
            user = ctx.author
        embed = Embed(title="Informations de l'utilisateur", color=0x00ff00)   
        embed.add_field(name="Pseudo", value=f"{user.display_name}#{user.discriminator}", inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Bot ?", value=user.bot, inline=True)
        embed.add_field(name="Créé le", value=user.created_at.strftime("%d/%m/%Y à %H:%M:%S"), inline=True)
        embed.set_footer(text=f"ID de l'utilisateur : {user.id}", icon_url=user.avatar.url)
        embed.add_field(name="Rejoint le", value=user.joined_at.strftime("%d/%m/%Y à %H:%M:%S"), inline=True)
        roles_value = " ".join([role.mention for role in user.roles]) if user.roles else "Pas de rôles"
        embed.add_field(name="Rôles", value=roles_value, inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        embed.add_image(user.avatar.url)
        await ctx.send(embed=embed)


def setup(bot):
    Userinfo(bot)
