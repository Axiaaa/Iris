from interactions import *
from utils.db_cmds import DB_commands
from utils.db import PydanticObjectId

class DelSanctions(Extension) :

    @slash_command(
        name="delsanctions",
        description="Supprime les sanctions d'un utilisateur",
        default_member_permissions= Permissions.ADMINISTRATOR
    )
    @slash_option(
        name="id",
        description="Id de la sanction à retirer",
        opt_type=OptionType.STRING,
        required=True
    )
    async def delsanctions(self, ctx : InteractionContext, id : str):
        await DB_commands.DB_del_sanction(ctx, PydanticObjectId(id))
        await ctx.respond("La sanction a bien été supprimée !", ephemeral=True)

def setup(bot):
    DelSanctions(bot)