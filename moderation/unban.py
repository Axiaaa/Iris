from interactions import *
from utils.db_cmds import DB_commands

class Unban(Extension) :

    @slash_command(
        name="unban",
        description="Unban un utilisateur du serveur",
        default_member_permissions= Permissions.ADMINISTRATOR
    )
    @slash_option(
        name="utilisateur",
        description="Utilisateur à unban",
        opt_type=OptionType.USER,
        required=True
    )
    @slash_option(
        name="raison",
        description="Raison du ban",
        opt_type=OptionType.STRING,
        required=True
    )
    async def unban(self, ctx : InteractionContext, utilisateur : User, raison : str = None):

        try :
            if not utilisateur :
                await ctx.respond("Cet utilisateur n'existe pas !", ephemeral=True)
                return
            if utilisateur.id == ctx.author.id:
                await ctx.respond("Vous ne pouvez pas vous unban vous-même !", ephemeral=True)
                return
            
            await ctx.guild.unban(utilisateur)
            embed = Embed(
                title="Unban",
                description=f"<@{utilisateur.id}> a bien été unban !",
                timestamp=Timestamp.now(),
                color= "#32CD32",
                thumbnail=utilisateur.avatar_url
            )
            if raison :
                embed.add_field(name="Raison", value=raison, inline=False)
            await ctx.channel.send(embed=embed)
            await ctx.respond("Fait !", ephemeral=True)
            await DB_commands.DB_add_unban(ctx, raison, utilisateur)

        except errors.NotFound :
            await ctx.respond("Cet utilisateur n'est pas bannis !", ephemeral=True)
        except errors.Forbidden : 
            await ctx.respond("Je n'ai pas réussi à unban cette personne. Veillez à ce que mon rôle soit bien positioné", ephemeral=True)
        
        #TODO : 
        #DATABASE & LOGS
def setup(bot):
    Unban(bot)