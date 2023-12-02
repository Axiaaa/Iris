from interactions import * 
from const import STARBOARD_REAC_COUNT, STARBOARD_CHANNEL_ID


class Starboard(Extension):


    @listen(events.MessageReactionAdd)
    async def starboard(self, event : events.MessageReactionAdd):
        if event.reaction_count == STARBOARD_REAC_COUNT and event.emoji.name == "⭐":
            message = event.message
            embed = Embed(
                title=f"De {message.author.display_name}",
                description=message.content,
                color=Color.from_hex("#2596be"),
                timestamp=message.created_at,
                thumbnail=message.author.avatar_url,
            )
            embed.set_footer(text=f"Message envoyé dans {message.channel.name}")
            embed.set_author(name="⭐ Starboard ⭐")
            components = [
                Button(
                    style=ButtonStyle.URL,
                    label="Aller au message",
                    url=message.jump_url,
                )
            ]
            starboard_channel = self.bot.get_channel(STARBOARD_CHANNEL_ID)
            await starboard_channel.send(embed=embed, components=components)

        
def setup(bot):
    Starboard(bot)