from interactions import *
from utils.db_cmds import DB_commands

class ModLogs(Extension) :

    @slash_command(
        name="modlogs",
        description="Affiche les logs de modération du serveur",
        default_member_permissions= Permissions.MANAGE_MESSAGES and Permissions.KICK_MEMBERS
    )
    @slash_option(
        name="utilisateur",
        description="Montre les logs de cet utilisateur",
        opt_type=OptionType.USER,
        required=True
    )
    async def modlogs(self, ctx : InteractionContext, utilisateur : User):

        if not utilisateur :
            await ctx.respond("Cet utilisateur n'existe pas !", ephemeral=True)
            return
        embed = Embed(
            title="Logs de modération",
            description=f"Logs de modération de <@{utilisateur.id}>",
            timestamp=Timestamp.now(),
            color= "#2596be",
            thumbnail=utilisateur.avatar_url
        )
        final_embed = await DB_commands.DB_get_logs(ctx, utilisateur, embed)
        await ctx.send(embed=final_embed)

def setup(bot):
    ModLogs(bot)