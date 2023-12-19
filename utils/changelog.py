from interactions import is_owner, Modal, ModalContext, ParagraphText, ShortText, SlashContext, slash_command,Embed,Permissions, Extension
from const import BOT_VERSION



class Changelog(Extension) : 

    is_owner()
    @slash_command(name="bot_changelog", description="Ajoute un changelog pour le bot")
    async def bot_changelog(self, ctx: SlashContext):
        my_modal = Modal(
        ShortText(label="Version",
                    custom_id="version",
                    placeholder=f"{BOT_VERSION}",
                    required=True),

        ParagraphText(label="Changelog",
                      custom_id="changelogtext",
                      placeholder="Entrez les changements",
                      required=True),
                      title="Ajouter un changelog")
    
        await ctx.send_modal(modal=my_modal)
        modal_ctx: ModalContext = await ctx.bot.wait_for_modal(my_modal)
        embed = Embed(title="Nouveau changelog !\t:tada:", description=f"\nChangements apportés par cette mise à jour :\n\n {modal_ctx.responses['changelogtext']}", color="#2596be")
        embed.set_footer(text=f"Iris {BOT_VERSION}", icon_url=self.bot.user.avatar_url)
        await ctx.channel.send(content= "<@&1182417319557873694>", embed=embed)
        await ctx.send("Changelog ajouté !", ephemeral=True)
        await modal_ctx.send("Changelog ajouté !", ephemeral=True)
        
def setup(bot): 
    Changelog(bot)