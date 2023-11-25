from interactions import *
from random import choice
from const import COOLDOWN_TIME_IN_SECS

def PierreFeuilleCiseaux(choix: str):
        """
        Fait une partie de pierre feuille ciseaux

        Args:
            choix (str): Le choix du joueur

        Returns:
            str: Le résultat de la partie
        """
        x = choice(["pierre", "papier", "ciseaux"])
        if (x == "pierre" and choix == "papier") or (x == "papier" and choix == "ciseaux") or (x == "ciseaux" and choix == "pierre"):
            return "w"
        elif (x == "pierre" and choix == "ciseaux") or (x == "papier" and choix == "pierre") or (x == "ciseaux" and choix == "papier"):
            return "l"
        else:
            return "d"
        
class Shifumi(Extension):

    @slash_command(name="shifumi", description="Lance une partie de shifumi contre le bot")
    @cooldown(bucket=Buckets.DEFAULT,rate=1, interval=COOLDOWN_TIME_IN_SECS)
    async def shifumi(self, ctx: InteractionContext):
        """
        Lance une partie de shifumi contre le bot

        Args:
            ctx (InteractionContext): Le contexte
        
        Returns:
            None
        """
        buttons : list[ActionRow] = [
        ActionRow(
            Button(
                style=ButtonStyle.GREEN, 
                custom_id=f"{ctx.user.id}_shifumi_pierre",
                emoji=":rock:"
            ),
            Button(
                style=ButtonStyle.DANGER,
                custom_id=f"{ctx.user.id}_shifumi_papier",
                emoji=":roll_of_paper:"            
            ),
            Button(
                style=ButtonStyle.BLUE,
                emoji=":scissors:",
                custom_id=f"{ctx.user.id}_shifumi_ciseaux"

            ))       
        ]
        await ctx.send(embed=Embed(
            title=f"Shifumi avec {ctx.author.display_name}",
            description="**Pierre** :rock:\n\n**Feuille** :roll_of_paper:\n\n**Ciseaux** :scissors:\n\nCliquez sur un des boutons pour choisir ? :arrow_heading_down:"), components=buttons)
        

    @listen(event_name="on_component")
    async def button_ciseaux(self, event): 

        x = event.ctx.custom_id.split("_")
        if f"{event.ctx.author.id}" == x[0] : 
            match x[2] :
                case "ciseaux" :
                    resultat = PierreFeuilleCiseaux("ciseaux")
                    if resultat == "l":
                        await event.ctx.edit_origin(components=(), embed=Embed(
                            title="Défaite",
                            description=f":scissors:\t**VS**\t:rock:\n\nVous avez perdu car j'ai choisi de faire la pierre ! :smiling_imp:",
                            color="#FF0000"
                        ))
                    elif resultat == "w":
                        await event.ctx.edit_origin(components=(),embed=Embed(
                            title="Victoire",
                            description=f":scissors:\t**VS**\t:roll_of_paper:\n\nVous avez gagné car j'ai choisi de faire la feuille !\nBien joué :tada:",
                            color= "#32CD32"
                        ))
                    elif resultat == "d":
                        await event.ctx.edit_origin(components=(),embed=Embed(
                        title="Egalité !",
                        description=f":scissors:\t**VS**\t:scissors:\n\nJ'ai choisi de faire les ciseaux et vous aussi ! On rejoue ? :stuck_out_tongue_winking_eye:"
                        ))
                case "pierre" :
                    resultat = PierreFeuilleCiseaux("pierre")
                    if resultat == "l":
                        await event.ctx.edit_origin(components=(), embed=Embed(
                            title="Défaite",
                            description=f":rock:\t**VS**\t:roll_of_paper:\n\nVous avez perdu car j'ai choisi de faire la feuille ! :smiling_imp:",
                            color="#FF0000"
                        ))
                    elif resultat == "w":
                        await event.ctx.edit_origin(components=(),embed=Embed(
                            title="Victoire",
                            description=f":rock:\t**VS**\t:scissors:\n\nVous avez gagné car j'ai choisi de faire les ciseaux !\nBien joué :tada:",
                            color= "#32CD32"
                        ))
                    elif resultat == "d":
                        await event.ctx.edit_origin(components=(),embed=Embed(
                        title="Egalité !",
                        description=f":rock:\t**VS**\t:rock:\n\nJ'ai choisi de faire la pierre et vous aussi ! On rejoue ? :stuck_out_tongue_winking_eye:"
                        ))
                case "papier" :
                    resultat = PierreFeuilleCiseaux("pierre")
                    if resultat == "l":
                        await event.ctx.edit_origin(components=(), embed=Embed(
                            title="Défaite",
                            description=f":roll_of_paper:\t**VS**\t:scissors:\n\nVous avez perdu car j'ai choisi de faire les ciseaux ! :smiling_imp:",
                            color="#FF0000"
                        ))
                    elif resultat == "w":
                        await event.ctx.edit_origin(components=(),embed=Embed(
                            title="Victoire",
                            description=f":roll_of_paper:\t**VS**\t:rock:\n\nVous avez gagné car j'ai choisi de faire la pierre !\nBien joué :tada:",
                            color= "#32CD32"
                        ))
                    elif resultat == "d":
                        await event.ctx.edit_origin(components=(),embed=Embed(
                        title="Egalité !",
                        description=f":roll_of_paper:\t**VS**\t:roll_of_paper:\n\nJ'ai choisi de faire la feuille et vous aussi ! On rejoue ? :stuck_out_tongue_winking_eye:"
                        ))
        else : 
            if x[1] != "shifumi" :
                return
            await event.ctx.send("Vous ne pouvez pas intéragir avec le jeu des autres !", ephemeral=True)

def setup(bot):
    Shifumi(bot)