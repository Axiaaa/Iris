from interactions import Client, Extension, OptionType, slash_command, slash_option, InteractionContext, listen
from interactions import ChannelType, PermissionOverwrite, Permissions, ButtonStyle, Button, ActionRow, Embed, Timestamp
import logging
from utils.db_cmds import DB_commands  # Assurez-vous que ce module est correctement implémenté

class Tickets(Extension): 
    def __init__(self, client: Client):
        self.client = client

    @slash_command(
        name="ticket",
        description="Crée un ticket",
    )

    @slash_option(
    name="raison",
    description="La raison de votre ticket",
    opt_type=OptionType.STRING,
    required=True
    )

    async def ticket(self, ctx: InteractionContext, raison: str):
        if await DB_commands.check_ticket(ctx, f"{ctx.author.id}"):
            await ctx.send("Vous avez déjà un ticket d'ouvert !", ephemeral=True)
            return

        guild = ctx.guild
        ticket_channel = await ctx.guild.create_channel(
            name=f"ticket-{ctx.author.username}",
            category=ctx.guild.get_channel(1186809443086766111),  # ID de la catégorie pour les tickets
            topic=f"Ticket de {ctx.author.username} pour {raison} | {ctx.author.id}",
            channel_type=ChannelType.GUILD_TEXT
        )
        await ticket_channel.set_permission(ctx.guild.get_role(1109476455731179522), view_channel=False)  # ID du rôle @everyone
        await ticket_channel.set_permission(ctx.author, view_channel=True)

        embed = Embed(
            title=f"Ticket de {ctx.author.username}",
            thumbnail=ctx.author.avatar_url,
            description=f"Vous avez créé ce ticket pour la raison suivante : {raison}\n\nUn membre du staff va vous répondre dans les plus brefs délais.",
            color=0x2596be,
            timestamp=Timestamp.now()
        )
        embed.set_footer(text=f"ID du ticket : {ticket_channel.id}")
        buttons = [
            ActionRow(
                Button(
                    style=ButtonStyle.DANGER, 
                    custom_id="ticket_close",
                    label="Fermer le ticket"
                )
            )
        ]
        msg = await ticket_channel.send(embed=embed, components=buttons)
        await msg.pin()
        await ctx.send("Ticket créé !", ephemeral=True)
        await DB_commands.create_ticket(ctx, ticket_channel)
        logging.info(f"Ticket {ticket_channel.name} créé par {ctx.author.username}")

    @listen()
    async def on_button_click(self, event: InteractionContext):
        if event.custom_id == "ticket_close":
            channel = event.channel
            await channel.set_permissions(event.user, read_messages=False)
            buttons = [
                ActionRow(
                    Button(
                        style=ButtonStyle.GREEN,
                        custom_id="ticket_reopen",
                        label="Rouvrir le ticket"
                    ),
                    Button(
                        style=ButtonStyle.DANGER,
                        custom_id="ticket_delete",
                        label="Supprimer le ticket"
                    ),
                    Button(
                        style=ButtonStyle.BLUE,
                        custom_id="ticket_transcript",
                        label="Transcrire le ticket"
                    )
                )
            ]
            await event.channel.send("Le ticket a été fermé.", components=buttons)
            await DB_commands.change_ticket_status(event.ctx, f"{event.channel.id}", "closed")

        elif event.custom_id == "ticket_delete":
            await DB_commands.delete_ticket(event.ctx, f"{event.channel.id}")
            await event.channel.delete()

        elif event.custom_id == "ticket_reopen":
            # Ajoutez ici la logique pour rouvrir le ticket
            await DB_commands.change_ticket_status(event.ctx, f"{event.channel.id}", "reopened")
            await event.channel.send("Le ticket a été rouvert.")

        elif event.custom_id == "ticket_transcript":
            # Ajoutez ici la logique pour transcrire le ticket
            await event.channel.send("La transcription du ticket est en cours...")

def setup(bot):
    Tickets(bot)
