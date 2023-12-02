from interactions import *
from utils.db_cmds import DB_commands

class Warn(Extension):

    @slash_command(name="warn",
                    description="Warn un membre",
                    default_member_permissions= Permissions.KICK_MEMBERS)
    @slash_option(name="member",
                description="Membre à warn",
                opt_type=OptionType.MENTIONABLE,
                required=True)
    @slash_option(name="reason",
                description="Raison du warn",
                opt_type=OptionType.STRING,
                required=True)
    async def warn(self, ctx : InteractionContext, member : Member, reason : str):
        if member not in ctx.guild.members :
            await ctx.respond("Cette personne n'est pas sur le serveur !", ephemeral=True)
            return
        if member == ctx.author :
            await ctx.respond("Vous ne pouvez pas vous warn vous-même !", ephemeral=True)
            return
        if member.bot :
            await ctx.respond("Vous ne pouvez pas warn un bot !", ephemeral=True)
            return
        if member.has_permission(Permissions.BAN_MEMBERS) :
            await ctx.respond("Vous ne pouvez pas warn cette personne !", ephemeral=True)
            return
        await member.send(f"Vous avez été warn de {ctx.guild.name} pour la raison suivante : {reason}")
        await DB_commands.DB_add_warn(ctx, reason, member)
        embed = Embed(
            title="Warn",
            description=f"{member.mention} a été warn !",
            timestamp=Timestamp.now(),
            color= "#2596be",
            thumbnail=member.avatar_url
        )
        embed.add_field(name="Raison", value=reason, inline=False)
        await ctx.channel.send(embed=embed)
        await ctx.respond("Fait !", ephemeral=True)

def setup(bot):
    Warn(bot)