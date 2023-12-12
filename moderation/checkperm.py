from interactions import *


class CheckPerm(Extension):


    @slash_command(
        name="checkperm",
        description="Vérifie les permissions d'un utilisateur",
        default_member_permissions=Permissions.MANAGE_MESSAGES
        )
    @slash_option(
        name="user",
        description="L'utilisateur dont vous voulez voir les permissions",
        opt_type=OptionType.USER,
        required=True
        )
    async def checkperm(self, ctx: InteractionContext, user: Member):
        """
        Vérifie les permissions d'un utilisateur

        Args:
            ctx (InteractionContext): Le contexte
            user (Member, optional): L'utilisateur. Defaults to None.
        
        Returns:
            None
        """
        embed = Embed(title="Permissions de l'utilisateur", color=0x00ff00)
        perm = str(user.guild_permissions).lower()[12:].split('|')
        for i in range(len(perm)):
            perm[i] = perm[i].replace('_', ' ')
            perm[i] = perm[i].capitalize()
            if perm[i].isdigit():
                perm[i] = perm[i].replace(perm[i], '')
        embed.add_field(name="Permissions", value='\n'.join(perm))
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=f"ID: {user.id}")
        embed.timestamp = Timestamp.now()
        await ctx.send(embed=embed)