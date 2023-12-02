from interactions import *


class Clear(Extension) :

    @slash_command("clear", description="Supprime un nombre de messages", default_member_permissions=Permissions.BAN_MEMBERS)
    @slash_option(
        name="nombre_messages",
        description="Nombre de messages à supprimer",
        required=True,
        max_value=50,
        opt_type=OptionType.INTEGER)
    async def clear(self, ctx : SlashContext, nombre_messages : int):
        try : 
            await ctx.channel.purge(nombre_messages)
            await ctx.send(f"J'ai bien supprimé {nombre_messages} messages !", ephemeral=True)
        except errors.HTTPException :
            await ctx.send("Une erreur est survenue !", ephemeral=True)

def setup(bot):
    Clear(bot)