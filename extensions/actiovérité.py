from interactions import *
import random 


actions = [
    "Envoyez un mème drôle dans le chat.",
    "Faites une imitation écrite d'une célébrité connue.",
    "Faites une déclaration d'amour à un objet inanimé dans le chat.",
    "Énumérez trois choses que vous appréciez chez chaque personne dans le chat.",
    "Faites une blague écrite et partagez-la dans le chat.",
    "Partagez une photo embarrassante de vous dans le chat.",
    "Racontez une histoire drôle et folle qui vous est arrivée récemment dans le chat.",
    "Inventez un slogan hilarant pour une marque fictive dans le chat.",
    "Partagez une astuce ou un conseil étrange mais utile dans le chat.",
    "Faites semblant d'être un animateur de télévision et présentez une émission fictive dans le chat.",
     "Faites une danse improvisée dans votre chambre et partagez une vidéo dans le chat.",
    "Chantez une chanson populaire en utilisant un accent étranger et enregistrez un message audio dans le chat.",
    "Imitez une personne célèbre de votre choix en écrivant une courte conversation dans le chat.",
    "Faites un compliment sincère à chaque personne du groupe dans le chat.",
    "Partagez une blague drôle ou un jeu de mots dans le chat.",
    "Créez un dessin rapide et partagez-le dans le chat.",
    "Racontez une anecdote drôle ou embarrassante qui vous est arrivée récemment dans le chat.",
    "Inventez un nom de produit bizarre et écrivez une description humoristique pour le vendre dans le chat.",
    "Donnez un conseil étrange mais potentiellement utile à chaque personne du groupe dans le chat.",
    "Prétendez être un animateur de télévision et interviewez un membre du groupe en posant des questions amusantes dans le chat.",
    "Faites un poème d'amour improvisé pour une personne du groupe.",
    "Inventez une histoire hilarante en utilisant les mots choisis par les autres membres.",
    "Faites un discours passionné sur un sujet aléatoire choisi par les autres membres.",
    "Imitez le style de danse d'une célébrité de votre choix.",
    "Décrivez une expérience de voyage fictive incroyablement extravagante.",
    "Faites une série d'acrobates (sauts, pirouettes, etc.) devant votre webcam.",
    "Faites un dessin à l'aveugle en utilisant la souris ou le clavier de votre ordinateur.",
    "Jouez une scène d'un film célèbre en utilisant des objets trouvés dans votre environnement.",
    "Faites un tour de magie improvisé avec des objets du quotidien.",
    "Faites semblant d'être un présentateur de talk-show et interviewez un membre du groupe."
]

vérités = [
    "Quelle est la dernière chose embarrassante que vous avez faite en ligne ?",
    "Quel est le secret le plus étrange que vous avez gardé pour vous ?",
    "Quel est votre plus grand regret en matière de messagerie ou de réseau social ?",
    "Avez-vous déjà fait semblant de liker un message juste pour faire plaisir à quelqu'un ?",
    "Quelle est la chose la plus bizarre que vous avez recherchée sur Internet récemment ?",
    "Quelle est la plus grande bêtise que vous ayez faite dans un chat ou sur les réseaux sociaux ?",
    "Quelle est la rumeur la plus folle que vous avez propagée ou entendue en ligne ?",
    "Quel est le pire commentaire que vous avez jamais écrit ou reçu sur les réseaux sociaux ?",
    "Avez-vous déjà utilisé un faux compte ou une fausse identité en ligne ?",
    "Quelle est la chose la plus embarrassante que vous avez accidentellement envoyée à la mauvaise personne dans un chat ou un message ?",
    "Quelle est la chose la plus étrange que vous avez recherchée sur Internet récemment ?",
    "Avez-vous déjà eu un compte de réseau social secret ? Si oui, racontez-nous à ce sujet.",
    "Quelle est la pire chose que vous ayez jamais envoyée par accident à la mauvaise personne dans un chat ou un message ?",
    "Avez-vous déjà prétendu aimer un film ou une série que vous détestiez en réalité ?",
    "Quelle est la rumeur la plus folle que vous ayez entendue sur vous-même en ligne ?",
    "Avez-vous déjà fait une capture d'écran d'un message embarrassant de quelqu'un d'autre ?",
    "Quelle est la chose la plus drôle ou bizarre que vous ayez postée sur les réseaux sociaux ?",
    "Avez-vous déjà regretté un commentaire que vous avez publié en ligne ?",
    "Avez-vous déjà créé un faux profil en ligne ? Si oui, dans quel but ?",
    "Quel est le message le plus embarrassant que vous ayez envoyé à un membre du groupe ?",
    "Quelle est la chose la plus gênante que vous ayez fait devant une foule ?",
    "Quelle est la plus grosse bêtise que vous ayez faite dans un contexte professionnel ou scolaire ?",
    "Quelle est votre plus grande peur irrationnelle ?",
    "Avez-vous déjà dit un mensonge énorme pour vous sortir d'une situation difficile ?",
    "Quelle est la chose la plus folle que vous ayez mangée par curiosité ?",
    "Quel est votre pire souvenir de vacances ou de voyage ?",
    "Avez-vous déjà eu une expérience paranormale ou surnaturelle ?",
    "Quelle est la pire punition que vous ayez jamais reçue quand vous étiez enfant ?",
    "Avez-vous déjà eu un béguin pour quelqu'un du groupe ?",
    "Quelle est la chose la plus embarrassante que vous ayez postée sur les réseaux sociaux ?",
    "Quel est le pire conseil que vous ayez jamais donné à quelqu'un en ligne ?",
    "Avez-vous déjà partagé un faux article ou une fausse nouvelle en ligne sans le vérifier ?",
    "Quelle est la chose la plus étrange que vous avez achetée en ligne ?",
    "Avez-vous déjà piraté un compte ou tenté de le faire ?",
    "Quelle est la chose la plus embarrassante que vous ayez découverte à votre sujet en ligne ?",
    "Avez-vous déjà été victime d'une arnaque en ligne ?",
    "Quelle est la chose la plus choquante que vous ayez trouvée en fouillant le profil de quelqu'un d'autre en ligne ?",
    "Avez-vous déjà été banni ou suspendu d'une plateforme en ligne ?"
]

class AouV(Extension):
    @slash_command(name="action_ou_verite", description="Joue à Action ou Vérité")
    async def aouv(self, ctx: InteractionContext):
        """
        Joue à Action ou Vérité

        Args:
            ctx (InteractionContext): [description]

        Returns:
            None 
        """
        embed=Embed(
            title="Action ou Vérité ?"
        )
        buttons : list[ActionRow] = [
        ActionRow(
            Button(
                style=ButtonStyle.GREEN, 
                custom_id="aouv_a",
                emoji=":crossed_swords:",
                label="Action"
            ),
            Button(
                style=ButtonStyle.DANGER,
                custom_id="aouv_v",
                emoji=":grey_question:",
                label="Vérité"       
            ),)       
        ]
    
        self.msg = await ctx.send(embed=embed, components=buttons)

    @component_callback("aouv_a")
    async def aouv_a(self, ctx: InteractionContext):
        embed=Embed(
            title="Action",
            description=f"**{random.choice(actions)}**",
            color=0x00ff00,
            footer="Action générée avec ChatGPT."
        )
        await self.msg.edit(components=[], embed=embed)
        

    @component_callback("aouv_v")
    async def aouv_v(self, ctx: InteractionContext):
        embed=Embed(
            title="Vérité",
            description=f"**{random.choice(vérités)}**",
            color=0xff0000,
            footer="Vérité générée avec ChatGPT."
        )
        await self.msg.edit(components=[], embed=embed)
    


def setyp(bot):
    AouV(bot)