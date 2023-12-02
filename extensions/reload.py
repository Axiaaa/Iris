import interactions, os, logging
from interactions import is_owner

class Reload(interactions.Extension): 

    is_owner()
    @interactions.slash_command(
            name="reload", 
            description="Cette commande permet de recharger les extensions du bot."
            )
    async def reload(self, ctx : interactions.InteractionContext):
        def reload_extensions(bot, folder, prefix="", exclude_files=[]):
            """
            
            Cette commande permet de recharger les extensions (fichers sources) du bot.
            
            Args:
                bot (interactions.Client): Client du bot
                folder (str): Dossier contenant les extensions
                prefix (str, optional): Préfixe des extensions. Defaults to "".
                exclude_files (list, optional): Fichiers à exclure. Defaults to [].
            Retourne :
                None
            """
            extensions = [file.replace(".py", "") for file in os.listdir(folder) if file.endswith(".py") and file not in exclude_files]
            for ext in extensions:
                bot.reload_extension(f"{prefix}{ext}")
                logging.debug(f"{ext} a été rechargé !")

        reload_extensions(self.bot, "ext", "ext.")
        reload_extensions(self.bot, "utils", "utils.", exclude_files=["db.py"])
        reload_extensions(self.bot, "moderation", "moderation.")
        await ctx.respond(content="Fait !", ephemeral=True)

def setup(bot): 
    Reload(bot)