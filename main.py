from typing import Final
import os
import audioop
from dotenv import load_dotenv
from nextcord import Intents, Client, Message
from response import get_response

# Load token from safe file
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# BOT_SETUP
intents: Intents = Intents.default()
intents.message_content = True #NOQA
client: Client = Client(intents=intents)

# Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled prbably)')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response: str= get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Handling the startup for the bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    user_message: str = message.content
    
    # Bot only responds if message starts with "!"
    if not user_message.startswith("!"):
        return
    
    # Remove "!" before message is processed
    user_message = user_message[1:]

    print(f'[{message.channel}] {message.author}: "{user_message}"')

    # Call send_message so the bot responds
    await send_message(message, user_message)

# Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()