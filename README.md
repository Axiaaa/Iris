# Iris

Iris est un bot multifonction dévelopé par moi-même dans le but d'apprendre et de partager mes connaissances.
La majorité du code est réalise en stream :

### https://www.twitch.tv/nephtyslovesnipe

Pour le moment, Iris est à un stade d'alpha. Cependant, vous pouvez créer des PR ou des issues si vous rencontrez des problèmes avec le code actuel.

## Le bot n'est pas encore invitable
Si vous souhaitez tout de même le tester, vous pouvez soit cloner le repo sur votre machine, soit rejoindre le serveur de test/support : https://discord.gg/ZedGy4pF5A

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :

- Python (version >= 3.10)
- MongoDB (pour la base de données)
- Visual studio build tools 2022 et les composants c++
- Un compte Discord avec un bot créé dans le [Portail des Développeurs Discord](https://discord.com/developers/applications) [Uniquement pour la phase de test]

## Installation

1. **Cloner le dépôt :**

   ```
   git clone https://github.com/Axiaaa/Iris.git
   cd Iris
   ```

2. **Configurer les variables d'environnement :**
   Créez un fichier `.env` à la racine du projet et configurez les variables nécessaires (par exemple, le token du bot, l'URL de la base de données, etc.).
   Vous pouvez voir les variables d'env nécessaires au fonctionnement du bot dans le ficher `const.py`.

4. **Lancer le bot :**
   ```
   python main.py
   ```

## Frameworks et Bibliothèques Utilisés

- [discord-py-interactions](https://github.com/discord-py-interactions/discord-py-interactions) pour interagir avec l'API Discord.
- [MongoDB](https://www.mongodb.com/) pour la gestion de la base de données.
- [Motor](https://motor.readthedocs.io/en/stable/) pour l'interface asynchrone avec MongoDB.
- [Beanie](https://roman-right.github.io/beanie/) pour l'ORM avec MongoDB.

## Commandes Disponibles

- `/8ball` : Pose une question à une boule magique.
- `/action_ou_verite` : Joue à action ou vérité.
- `/bagarre` : C'est l'heure de la bagarre !
- `/dire [texte]` : Fais parler le bot.
- `/ticket [raison]` : Ouvre un ticket.
- `/help` : Affiche toutes les commandes disponibles.
- `/info` : Affiche les informations du bot.
- `/ping` : Ping le bot.
- `/reload` : Cette commande permet de recharger les extensions du bot.
- `/roll` : Lance un dé.
- `/serveurinfo` : Affiche les informations du serveur.
- `/shifumi` : Lance une partie de shifumi contre le bot.
- `/userinfo [user]` : Affiche les informations d'un utilisateur.
- `/warn [member] [reason]` : Ajoute un warn à un membre pour une raison spécifiée.
- `/mute [member] [duration] [unit] [reason]` : Mute un membre pour une durée déterminée.
- `/unmute [user]` : Unmute un membre mute.
- `/kick [member] [reason]` : Expulse un membre du serveur.
- `/ban [member] [reason]` : Bannit un membre du serveur.
- `/unban [user]` : Unban un utilisateur du serveur.
- `/checkperm [user]` : Vérifie les permissions d'un utilisateur.
- `/clear [NOMBRE MAX : 50]` : Supprime un nombre de messages.
- `/delsanctions` : Supprime les sanctions d'un utilisateur.
- `/modhelp` : Affiche l'aide pour les commandes de modération.
- `/modlogs` : Affiche les logs de modération du serveur.
- `/nick` : Change le pseudo d'un membre.

## Licence

**GNU GENERAL PUBLIC LICENSE**

**Permissions**

Modification
Distribution
Patent use
Private use

**Limitations**

Liability
Warranty

**Conditions**
License and copyright notice
State changes
Disclose source
Same license
