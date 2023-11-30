from interactions import *
from utils.db_cmds import DB_commands

class Kick(Extension):

    @slash_command(
            name="kick",
            description="Kick un membre du serveur",
            default_member_permissions= Permissions.KICK_MEMBERS)
    @slash_option(
        name="utilisateur",
        description="Utilisateur à kick",
        opt_type=OptionType.MENTIONABLE,
        required=True
    )
    @slash_option(
        name="raison",
        description="Raison du kick",
        opt_type=OptionType.STRING,
        required=False
    )
    async def kick(self, ctx : InteractionContext, utilisateur: Member, raison : str = None):

        try :
            if not utilisateur :
                await ctx.respond("Cet utilisateur n'existe pas !", ephemeral=True)
                return
            if utilisateur not in ctx.guild.members : 
                await ctx.respond("Cet utilisateur n'est pas présent sur ce serveur !", ephemeral=True)
                return
            if utilisateur.id == ctx.author.id:
                await ctx.respond("Vous ne pouvez pas vous kicker vous-même !", ephemeral=True)
                return
            
            await ctx.guild.kick(utilisateur, reason=raison)
            embed = Embed(
                title="Kick",
                description=f"<@{utilisateur.id}> a bien été kick !",
                timestamp=Timestamp.now(),
                color= "#32CD32",
                thumbnail=utilisateur.avatar_url
            )
            if raison : 
                embed.add_field("Raison :", raison)
            await ctx.channel.send(embed=embed)
            await ctx.respond("Fait !", ephemeral=True)
            await DB_commands.DB_add_kick(ctx, raison, utilisateur)

        except errors.Forbidden : 
            await ctx.respond("Je n'ai pas réussi à kicker cette personne. Veillez à ce que mon rôle soit bien positioné", ephemeral=True)
        

def setup(bot):
    Kick(bot)



