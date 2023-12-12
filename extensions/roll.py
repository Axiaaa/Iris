from interactions import *
from random import randint

class Roll(Extension):
    
    @slash_command(name="roll", description="Lance un dé")
    async def roll(self, ctx : InteractionContext):
        """
        Lance un dé

        Args:
            ctx (InteractionContext): Le contexte
        
        Returns:
            None
        """
        roll = randint(1, 6)
        await ctx.send(f"Tu as fait un {roll} 🎲 !")


def setup(bot):
    Roll(bot)
