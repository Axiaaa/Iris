from interactions import *



class Nick(Extension) :

    @slash_command("nick", description="Change le pseudo d'un membre", default_member_permissions=Permissions.MANAGE_NICKNAMES)
    @slash_option(
        name="pseudo",
        description="Nouveau pseudo",
        required=True,
        opt_type=OptionType.STRING)
    @slash_option(
        name="utilisateur",
        description="utilisateur",
        required=False,
        opt_type=OptionType.USER)
    async def change_pseudo(self, ctx : SlashContext, pseudo : str, utilisateur : Member = None):
        if utilisateur == None : 
            utilisateur = ctx.author
        await utilisateur.edit_nickname(new_nickname=pseudo)
        await ctx.send(f"Le pseudo de <@{utilisateur.id}> a bien été changé en {pseudo}", ephemeral=True)

def setup(bot):
    Nick(bot)
