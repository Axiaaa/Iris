from interactions import *
import random

class Eightball(Extension):


    responses = [
        "C'est certain.",
        "Sans aucun doute.",
        "Oui, absolument.",
        "Oui, définitivement.",
        "Il est certain.",
        "Il en est décidé ainsi.",
        "Très probable.",
        "Les perspectives sont bonnes.",
        "Non.",
        "Tout porte à le croire.",
        "Réponse floue, réessaie.",
        "Demande à nouveau plus tard.",
        "Mieux vaut ne pas te le dire maintenant.",
        "Je ne peux pas prédire cela pour le moment.",
        "Concentrez-vous et demandez à nouveau.",
        "Ne compte pas là-dessus.",
        "Ma réponse est non.",
        "Mes sources disent que non.",
        "Les perspectives ne sont pas bonnes.",
        "Très incertain.",
        "Je suis désolé, je ne peux pas répondre à ça.",
        "Les signes pointent vers une réponse négative.",
        "Les chances sont minces, voire inexistantes.",
        "Il vaudrait mieux ne pas y penser.",
        "Demande à quelqu'un d'autre, je ne suis pas sûr.",
        "Il est peu probable que cela se produise.",
        "La réponse est incertaine.",
        "Même le cosmos ne peut pas prédire cela.",
        "Les étoiles disent non.",
        "Le destin est contre toi.",
        "C'est peu probable, mais tout est possible.",
        "Ne mets pas trop d'espoir là-dedans.",
        "Il vaudrait mieux essayer autre chose.",
        "La probabilité est en ta faveur.",
        "Demande à nouveau plus tard pour une réponse plus claire.",
        "Axelle pense que oui...",
        "Axelle pense que non...",
    ]


    @slash_command(name="8ball", description="Pose une question à la boule magique")
    @slash_option(name="question", description="La question que vous voulez poser", opt_type=OptionType.STRING, required=True)
    async def eightball(self, ctx : InteractionContext, question : str):
            
        """
        Pose une question à la boule magique

        Args:
            ctx (InteractionContext): Le contexte
            question (str): La question que vous voulez poser

        Returns:
            None
        """

        embed = Embed(title=":8ball: 8ball",color=0x00ff00)
        embed.add_field(name="Question", value=question, inline=True)
        embed.add_field(name="Réponse", value=random.choice(self.responses))
        embed.set_footer(text=f"Posée par {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        embed.timestamp = Timestamp.now()
        await ctx.send(embed=embed)



def setup(bot):
    Eightball(bot)