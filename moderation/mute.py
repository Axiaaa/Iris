from interactions import * 
import datetime
from utils.db_cmds import DB_commands

class Mute(Extension):

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
    async def mute(self, ctx : SlashContext, user: Member, duree=float, unite= str, raison=None):
        try :
            if user.communication_disabled_until : 
                await ctx.send("Cette personne est déjà mute!", ephemeral=True)
                return
            if user not in ctx.guild.members :
                await ctx.send("Cette personne n'est pas sur le serveur !", ephemeral=True)
                return
            if user == ctx.author :
                await ctx.send("Vous ne pouvez pas vous mute vous-même !", ephemeral=True)
                return
            if user.bot :
                await ctx.send("Vous ne pouvez pas mute un bot !", ephemeral=True)
                return
            
            duree_mute = duree
            if unite == "Secondes" :
                duree = duree
            elif unite == "Minutes" :
                duree = duree * 60
            elif unite == "Heures" :
                duree = duree * 3600
            elif unite == "Jours" :
                duree = duree * 86400

            date = datetime.datetime.now() + datetime.timedelta(seconds=duree)
            await user.timeout(communication_disabled_until=date, reason=raison)
            await ctx.send(f"<@{user.id}> a bien été mute !", ephemeral=True)
            embed = Embed(title=f"Mute", description=f"<@{user.id}> a été mute!", thumbnail=user.avatar_url, color="#32CD32")
            if not raison:
                embed.add_field(name=f"Raison : ", value=f"{raison}\n")
            embed.add_field(name="Durée", value=f"{duree_mute} {unite.lower()}")
            await ctx.channel.send(embed=embed)
            await user.send(f"Vous avez été mute sur le serveur {ctx.guild.name}. Durée : {duree_mute} {unite.lower()}. Raison : {raison}")
            await DB_commands.DB_add_mute(ctx,str(duree_mute) + " " + unite.lower(), raison, user)

        except errors.Forbidden :
            await ctx.send("Je n'ai pas la permission de mute ce membre ! Veillez à ce que mon rôle soit placé plus haut que celui du membre que vous voulez kick.", ephemeral=True)
            return
        except errors.HTTPException :
            await ctx.send("La durée du mute est trop longue ! Durée max : 26 jours", ephemeral=True)
            return
        except errors.NotFound :
            await ctx.send("Cet utilisateur n'existe pas !", ephemeral=True)
            return

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
    async def unmute(self, ctx : SlashContext, user: Member, raison=None):
        try :
            if not user.communication_disabled_until :
                await ctx.send("Cette personne n'est pas mute !", ephemeral=True)
                return
            if user not in ctx.guild.members :
                await ctx.send("Cette personne n'est pas sur le serveur !", ephemeral=True)
                return
            if user == ctx.author :
                await ctx.send("Vous ne pouvez pas vous unmute vous-même !", ephemeral=True)
                return
            if user.bot :
                await ctx.send("Vous ne pouvez pas unmute un bot !", ephemeral=True)
                return

            await user.timeout(communication_disabled_until=None, reason=raison)
            await ctx.send(f"<@{user.id}> a bien été unmute !", ephemeral=True)
            embed = Embed(title=f"Unmute", description=f"<@{user.id}> a été unmute!", thumbnail=user.avatar_url, color="#32CD32")
            if not raison:
                embed.add_field(name=f"Raison : ", value=f"{raison}\n")
            await ctx.channel.send(embed=embed)
            await user.send(f"Vous avez été unmute sur le serveur {ctx.guild.name}. Raison : {raison}")
            await DB_commands.DB_add_unmute(ctx, raison, user)

        except errors.Forbidden :
            await ctx.send("Je n'ai pas la permission d'unmute ce membre ! Veillez à ce que mon rôle soit placé plus haut que celui du membre que vous voulez kick.", ephemeral=True)
            return
        except errors.NotFound :
            await ctx.send("Cet utilisateur n'existe pas !", ephemeral=True)
            return

def setup(bot):
    Mute(bot)