from interactions import *
import datetime
from utils.db_cmds import DB_commands

class Mute(Extension):
    DUREE_MAPPING = {
        "Secondes": 1,
        "Minutes": 60,
        "Heures": 3600,
        "Jours": 86400
    }
    MAX_MUTE_DURATION_SECONDS = 28 * 86400  # 28 jours

    async def _validate_user(self, ctx, user):
        if user not in ctx.guild.members:
            await ctx.send("Cette personne n'est pas sur le serveur !", ephemeral=True)
            return False
        if user == ctx.author:
            await ctx.send("Vous ne pouvez pas mute/unmute vous-même !", ephemeral=True)
            return False
        if user.bot:
            await ctx.send("Vous ne pouvez pas mute/unmute un bot !", ephemeral=True)
            return False
        return True

    @slash_command(
            name="mute",
            description="Mute un membre",
            default_member_permissions=Permissions.MUTE_MEMBERS)
    @slash_option(
        name="user",
        description="Membre à mute",
        required=True,
        opt_type=OptionType.USER)
    @slash_option(
        name="duree",
        description="Durée du mute",
        required=True,
        opt_type=OptionType.INTEGER)
    @slash_option(
        name="unite",
        description="Unité de la durée",
        required=True,
        opt_type=OptionType.STRING,
        choices=[
        SlashCommandChoice(name="Seconde", value="Secondes"),
        SlashCommandChoice(name="Minute", value="Minutes"),
        SlashCommandChoice(name="Heure", value="Heures"),
        SlashCommandChoice(name="Jour", value="Jours")])
    @slash_option(
        name="raison",
        description="Raison du mute",
        required=False,
        opt_type=OptionType.STRING)
    async def mute(self, ctx: SlashContext, user: Member, duree: int, unite: str, raison=None):
        if not await self._validate_user(ctx, user):
            return

        duree_seconds = duree * self.DUREE_MAPPING.get(unite, 1)
        if duree_seconds > self.MAX_MUTE_DURATION_SECONDS:
            await ctx.send("La durée du mute est trop longue ! Durée max : 28 jours", ephemeral=True)
            return

        try:
            date = datetime.datetime.now() + datetime.timedelta(seconds=duree_seconds)
            await user.timeout(communication_disabled_until=date, reason=raison)
            await ctx.send(f"<@{user.id}> a bien été mute !", ephemeral=True)
            embed = Embed(title="Mute", description=f"<@{user.id}> a été mute!", color="#2596be")
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="Durée", value=f"{duree} {unite.lower()}", inline=False)
            if raison:
                embed.add_field(name="Raison", value=raison, inline=False)
            await ctx.channel.send(embed=embed)
            await user.send(f"Vous avez été mute sur le serveur {ctx.guild.name}. Durée: {duree} {unite.lower()}. Raison: {raison}")
            await DB_commands.DB_add_mute(ctx, str(duree) + " " + unite.lower(), raison, user)
        except errors.Forbidden:
            await ctx.send("Je n'ai pas la permission de mute ce membre !", ephemeral=True)
        except errors.HTTPException:
            await ctx.send("Erreur lors de l'application du mute.", ephemeral=True)
        except errors.NotFound:
            await ctx.send("Cet utilisateur n'existe pas !", ephemeral=True)

    @slash_command(
            name="unmute",
            description="Unmute un membre",
            default_member_permissions=Permissions.MUTE_MEMBERS)
    @slash_option(
        name="user",
        description="Membre à unmute",
        required=True,
        opt_type=OptionType.USER)
    @slash_option(
        name="raison",
        description="Raison de l'unmute",
        required=False,
        opt_type=OptionType.STRING)
    async def unmute(self, ctx: SlashContext, user: Member, raison=None):
        if not await self._validate_user(ctx, user):
            return

        try:
            await user.timeout(communication_disabled_until=None, reason=raison)
            await ctx.send(f"<@{user.id}> a bien été unmute !", ephemeral=True)
            embed = Embed(title="Unmute", description=f"<@{user.id}> a été unmute!", color="#2596be")
            embed.set_thumbnail(url=user.avatar_url)
            if raison:
                embed.add_field(name="Raison", value=raison, inline=False)
            await ctx.channel.send(embed=embed)
            await user.send(f"Vous avez été unmute sur le serveur {ctx.guild.name}. Raison: {raison}")
            await DB_commands.DB_add_unmute(ctx, raison, user)
        except errors.Forbidden:
            await ctx.send("Je n'ai pas la permission d'unmute ce membre !", ephemeral=True)
        except errors.NotFound:
            await ctx.send("Cet utilisateur n'existe pas !", ephemeral=True)

def setup(bot):
    Mute(bot)