from interactions import *
from utils.db_cmds import *

class Ban(Extension):

    @slash_command(
            name="ban",
            description="Bannir un membre du serveur")
    @slash_option(
        name="utilisateur",
        description="Utilisateur à Ban",
        opt_type=OptionType.MENTIONABLE,
        required=True
    )
    @slash_option(
        name="raison",
        description="Raison du Ban",
        opt_type=OptionType.STRING,
        required=False
    )
    @slash_option(
        name="supprimer_message",
        description="Faut-il supprimer les messages de cet utilisateur ?",
        opt_type=OptionType.BOOLEAN,
        required=False
    )
    async def Ban(self, ctx : InteractionContext, utilisateur: Member, raison : str = None, supprimer_message = False):
        try :
            if not utilisateur :
                await ctx.respond("Cet utilisateur n'existe pas !", ephemeral=True)
                return
            if utilisateur.id == ctx.author.id:
                await ctx.respond("Vous ne pouvez pas vous bannir vous-même !", ephemeral=True)
                return
            if supprimer_message : 
                supprimer_message = 7
            await ctx.guild.ban(utilisateur, reason=raison, delete_message_days=supprimer_message)
            embed = Embed(
                title="Ban",
                description=f"<@{utilisateur.id}> a bien été bannis !",
                timestamp=Timestamp.now(),
                color= "#32CD32",
                thumbnail=utilisateur.avatar_url
            )
            if raison : 
                embed.add_field("Raison :", raison)
            await ctx.channel.send(embed=embed)
            await ctx.respond("Fait !", ephemeral=True)
            await DB_commands.DB_add_ban(ctx, raison, utilisateur)
        except errors.Forbidden : 
            await ctx.respond("Je n'ai pas réussi à bannir cette personne. Veillez à ce que mon rôle soit bien positioné", ephemeral=True)
        
        #TODO : 
        #DATABASE & LOGS

def setup(bot):
    Ban(bot)



