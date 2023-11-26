from interactions import *
import random

class Presence(Extension):

    @listen(event_name=events.Startup)
    async def presence(self, event : events.Startup):
        await self.presence_update(self.bot)

    @slash_command(name="presenceupdate", description="Change la présence du bot")
    async def presence_update_command(self, ctx : InteractionContext):
        await self.presence_update(self.bot)
        await ctx.respond(content="Fait !", ephemeral=True)

    async def presence_update(self, bot : Client):
          await self.bot.change_presence(
            status= random.choice([Status.ONLINE, Status.IDLE, Status.DND]),
            activity=Activity(
                name="NephtysLoveSnipe",
                type=ActivityType.STREAMING,
                url="https://www.twitch.tv/nephtyslovesnipe",
                
                # created_at=Timestamp.now()

                # assets=ActivityAssets(
                #     large_image="https://cdn.discordapp.com/embed/avatars/3.png?size=4096",
                #     large_text="NephtysLoveSnipe",
                #     small_image="nephtyslovesnipe",
                #     small_text="https://cdn.discordapp.com/embed/avatars/3.png?size=4096"
                # timestamps=ActivityTimestamps(
                #     start=Timestamp.now(),
                #     end=42
                # )
        ))


def setup(bot):
    Presence(bot)
