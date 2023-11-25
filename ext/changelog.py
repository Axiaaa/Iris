from interactions import *


class Changelog(Extension):
    
    
    async def owner_check(ctx: InteractionContext):
        return ctx.author.id == 240430740158939139

    @check(check=owner_check)
    @slash_command(name="bot_changelog", description="Ajoute un changelog pour le bot", default_member_permissions=Permissions.ADMINISTRATOR)
    async def bot_changelog(self, ctx: SlashContext):
        """
        Ajoute un changelog pour le bot

        Args:
            ctx (SlashContext): Le contexte

        Returns:
            None
        """
        my_modal = Modal(
        ShortText(label="Version",
                    custom_id="version",
                    placeholder=f"MINOR.MAJOR.PATCH",
                    required=True),

        ParagraphText(label="Changelog",
                        custom_id="changelogtext",
                        placeholder="Entrez les changements",
                        required=True),
                        title="Ajouter un changelog")
        
        await ctx.send_modal(modal=my_modal)
        modal_ctx: ModalContext = await ctx.bot.wait_for_modal(my_modal)
        embed = Embed(title="Nouveau changelog !\t:tada:", description=f"\nChangements apportés par cette mise à jour :\n\n {modal_ctx.responses['changelogtext']}")
        embed.set_footer(text=f"Pipo#4026 - {modal_ctx.responses['version']}", icon_url=self.bot.user.avatar_url)
        embed.timestamp = Timestamp.now()
        await ctx.channel.send(embed=embed)
        await modal_ctx.send("Changelog ajouté !", ephemeral=True)


def setup(bot):
    Changelog(bot)

