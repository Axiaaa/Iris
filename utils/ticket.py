from interactions import *
import logging
import json

class Tickets(Extension): 
   

    @slash_command(
        name="ticket",
        description="Crée un ticket"
        )
    @slash_option(
        name="raison",
        description="La raison de votre ticket",
        opt_type=OptionType.STRING,
        required=True
        )
    async def ticket(self, ctx: InteractionContext, raison: str):

        for channel in ctx.guild.get_channel(1185674072856731749).text_channels:
            if channel and channel.topic is not None:
                if channel.topic.endswith(str(ctx.author.id)):
                    await ctx.send("Vous avez déjà un ticket")
                    return
        ticket = await ctx.guild.create_channel(
            name=f"ticket-{ctx.author.username}",
            category=ctx.guild.get_channel(1185674072856731749),
            topic=f"Ticket de {ctx.author.username} pour {raison} | {ctx.author.id}",
            channel_type=ChannelType.GUILD_TEXT)
        await ticket.set_permission(ctx.guild.get_role(1179840761781567508), view_channel=False)
        await ticket.set_permission(ctx.author, view_channel=True)
        embed = Embed(
            title=f"Ticket de {ctx.author.username}",
            thumbnail=ctx.author.avatar_url,
            description=f"Vous avez crée ce ticket avec la raison suivante : {raison}\n\nUn membre du staff va vous répondre dans les plus brefs délais !",
            color="#2596be",
            timestamp=Timestamp.now()
            )
        buttons : list[ActionRow] = [
                ActionRow(
                    Button(
                        style=ButtonStyle.DANGER, 
                        custom_id="ticket_close",
                        emoji=":closed_lock_with_key:",
                        label="Fermer le ticket"
                    ))]
        msg = await ticket.send(embed=embed, components=buttons)
        await msg.pin()
        await ctx.send("Ticket crée !", ephemeral=True)

    @listen(event_name="on_component")
    async def button_ciseaux(self, event): 
        if event.ctx.custom_id == "ticket_close":
            await event.ctx.channel.set_permission(event.ctx.user, view_channel=False)
            await event.ctx.channel.send(embed=Embed(
                title="Ticket fermé :lock:",
                description=f"Le ticket a été fermé par {event.ctx.user.mention}",
                color="#2596be",
                timestamp=Timestamp.now()
                )
            )
            buttons : list[ActionRow] = [
                ActionRow(
                    Button(
                        style=ButtonStyle.GREEN, 
                        custom_id="ticket_reopen",
                        emoji=":unlock:",
                        label="Rouvrir le ticket"
                    ),
                    Button(
                        style=ButtonStyle.DANGER, 
                        custom_id="ticket_delete",
                        emoji=":put_litter_in_its_place:",
                        label="Supprimer le ticket"
                    ),
                    Button(
                        style=ButtonStyle.BLUE, 
                        custom_id="ticket_transcript",
                        emoji=":newspaper:",
                        label="Faire un transcript du ticket"
                    ))]
            await event.ctx.message.edit(components=buttons)
            return

        if event.ctx.custom_id == "ticket_delete":
            await event.ctx.channel.delete()
            logging.info(f"Ticket {event.ctx.channel.name} supprimé par {event.ctx.user.username}")
            return


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