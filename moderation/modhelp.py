from interactions import *



class ModHelp(Extension) :


    @slash_command("modhelp", description="Affiche l'aide pour les commandes de modération", default_member_permissions=Permissions.BAN_MEMBERS)
    async def modhelp(self, ctx : SlashContext):
        embed = Embed(
                title="Voici la liste de toutes les commandes de modération disponibles",
                footer=EmbedFooter(text="Bot créé par Nephtys, à contacter si besoin.", icon_url=self.bot.user.avatar_url))
        embed.add_field(name="/mute", value="Mute un membre")
        embed.add_field(name="/unmute", value="Unmute un membre")
        # embed.add_field(name="/delsanctions", value="Supprime les sanctions d'un utilisateur")
        embed.add_field(name="/nick", value="Change le pseudo d'un membre")
        embed.add_field(name="/clear", value="Supprime un nombre de messages")
        embed.add_field(name="/ban", value="Ban un membre")
        embed.add_field(name="/unban", value="Unban un membre")
        embed.add_field(name="/kick", value="Kick un membre")
        embed.add_field(name="/warn", value="Warn un membre")
        embed.add_field(name="/checkperm", value="Voir les permissions d'un membre")
        await ctx.send(embed=embed, ephemeral=True)
        
def setup(bot):
    ModHelp(bot)