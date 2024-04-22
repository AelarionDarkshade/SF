import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('p!spam'):
        spam_message = "Spamming message!"
        for _ in range(10):  # Change the range for more or fewer messages
            await message.channel.send(spam_message)
            await asyncio.sleep(1)  # Adjust the delay between messages

client.run('token', bot=False)
