from interactions import Client, CommandContext, Extension, OptionType, slash_command, ComponentContext, ButtonStyle, Button, ActionRow
from interactions import ChannelType, PermissionOverwrite, Permissions

GUILD_ID= #IDSERV
CATEGORY_ID=1185674072856731749

class TicketSystem(Extension):
    def __init__(self, client: Client) -> None:
        super().__init__()