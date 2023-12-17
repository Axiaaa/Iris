from interactions import *
from utils.db_cmds import DB_commands

class Userinfo(Extension):

    @slash_command(name="userinfo", description="Affiche les informations d'un utilisateur")
    @slash_option(name="user", description="L'utilisateur dont vous voulez voir les informations", opt_type=OptionType.USER )
    async def userinfo(self, ctx: InteractionContext, user: Member = None):
        if user is None:
            user = ctx.author
        """
        Affiche les informations d'un utilisateur

        Args:
            ctx (InteractionContext): Le contexte
            user (Member, optional): L'utilisateur. Defaults to None.
        
        Returns:
            None
        """

        # Obtiens le nombre de warns
        warn_count = await DB_commands.get_warn_count(ctx, user.id)

        embed = Embed(title="Informations de l'utilisateur", color=0x00ff00)
        pseudo_value = f"{user.display_name}#{user.discriminator}" if user.discriminator != 0 else f"{user.display_name}"
        embed.add_field(name="Pseudo", value=pseudo_value, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Bot ?", value="Oui" if user.bot else "Non", inline=True)
        embed.add_field(name="Créé le", value=user.created_at.strftime("%d/%m/%Y à %H:%M:%S"), inline=True)
        embed.add_field(name="Rejoint le", value=user.joined_at.strftime("%d/%m/%Y à %H:%M:%S"), inline=True)
        roles_value = " ".join([role.mention for role in user.roles]) if user.roles else "Pas de rôles"
        embed.add_field(name="Rôles", value=roles_value, inline=True)
        embed.add_field(name="Nombre de warns", value=str(warn_count), inline=True)

        embed.set_footer(text=f"ID de l'utilisateur : {user.id}", icon_url=user.avatar.url)
        embed.timestamp = Timestamp.now()
        embed.set_thumbnail(user.avatar.url)
        await ctx.send(embed=embed)

    async def get_warn_count(self, user_id):
        return await DB_commands.get_warn_count(user_id)

def setup(bot):
    Userinfo(bot)
