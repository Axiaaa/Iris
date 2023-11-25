from interactions import *

class Serverinfo(Extension):

    @slash_command(name="serveurinfo", description="Affiche les informations du serveur")
    async def serverinfo(self, ctx : InteractionContext):
        """
        Affiche les informations du serveur

        Args:
            ctx (InteractionContext): Le contexte

        Returns:
            None
        """
        embed = Embed(title="Informations du serveur", color=0x00ff00, thumbnail=EmbedAttachment(url=ctx.guild.icon.url))   
        embed.add_field(name="Nom du serveur", value=ctx.guild.name, inline=True)
        embed.add_field(name="Nombre de membres", value=ctx.guild.member_count, inline=True)
        embed.add_field(name="Nombre de rôles", value=len(ctx.guild.roles), inline=True)
        embed.add_field(name="Nombre de salons", value=len(ctx.guild.channels), inline=True)
        embed.add_field(name="Nombre de boosts", value=ctx.guild.premium_subscription_count, inline=True)
        embed.add_field("Créé le", value=ctx.guild.created_at.strftime("%d/%m/%Y à %H:%M:%S"), inline=True)
        embed.set_footer(text=f"ID du serveur : {ctx.guild.id}", icon_url=ctx.guild.icon.url)
        embed.timestamp = Timestamp.now()
        embed.add_field(name="Propriétaire", value=f"<@{ctx.guild._owner_id}>")
        embed.add_field(name="Rôles", value=", ".join([role.mention for role in ctx.guild.roles]))
        await ctx.send(embed=embed)
        





def setup(bot):
    Serverinfo(bot)
