from interactions import Client, Extension, OptionType, slash_command, slash_option, InteractionContext, listen
from interactions import ChannelType, PermissionOverwrite, Permissions, ButtonStyle, Button, ActionRow, Embed, Timestamp
import logging
from utils.db_cmds import DB_commands

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
            category=ctx.guild.get_channel(1185674072856731749),  # ID de la catégorie pour les tickets
            topic=f"Ticket de {ctx.author.username} pour {raison} | {ctx.author.id}",
            channel_type=ChannelType.GUILD_TEXT
        )
        await ticket_channel.set_permission(ctx.guild.get_role(1179840761781567508), view_channel=False)  # ID du rôle @everyone
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

    @listen(event_name="on_component")
    async def bouttons_tickets(self, event): 
        if event.ctx.custom_id == "ticket_close":
            # Définir les permissions pour masquer le canal à l'utilisateur
            await event.ctx.channel.set_permission(event.ctx.user, view_channel=False)
            await event.ctx.channel.send(embed=Embed(
                title="Ticket fermé :lock:",
                description=f"Le ticket a été fermé par {event.ctx.user.mention}",
                color="#2596be",
                timestamp=Timestamp.now()
            ))

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
                        label="Faire un transcript du ticket"
                    )
                )
            ]

            await event.ctx.channel.send("Le ticket a été fermé.", components=buttons)
            await DB_commands.change_ticket_status(event.ctx, f"{event.ctx.channel.id}", "closed")

        elif event.ctx.custom_id == "ticket_delete":
            await DB_commands.delete_ticket(event.ctx, f"{event.ctx.channel.id}")
            await event.ctx.channel.delete()

        elif event.custom_id == "ticket_reopen":
            # Ajoute ici la logique pour rouvrir le ticket
            await DB_commands.change_ticket_status(event.ctx, f"{event.ctx.channel.id}", "reopened")
            await event.ctx.channel.send("Le ticket a été rouvert.")

        elif event.custom_id == "ticket_transcript":
            # Ajoute ici la logique pour transcrire le ticket
            await event.ctx.channel.send("La transcription du ticket est en cours...")



                    # if event.ctx.custom_id == "ticket_reopen":
        #     await event.ctx.channel.set_permission(event.ctx.channel.topic[], view_channel=True)
        #     await event.ctx.channel.send(embed=Embed(
        #         title="Ticket réouvert :unlock:",
        #         description=f"Le ticket a été réouvert par {event.ctx.user.mention}",
        #         color="#2596be",
        #         timestamp=Timestamp.now()
        #         )
        #     )
        #     buttons : list[ActionRow] = [
        #         ActionRow(
        #             Button(
        #                 style=ButtonStyle.DANGER, 
        #                 custom_id="ticket_close",
        #                 emoji=":closed_lock_with_key:",
        #                 label="Fermer le ticket"
        #             ))]
        #     await event.ctx.message.edit(components=buttons)
        #     return


def setup(bot):
    Tickets(bot)
