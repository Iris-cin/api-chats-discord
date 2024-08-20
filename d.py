import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('!cat'):
        api_key = 'votre_cle_api'  # Utilisez une clé valide
        response = requests.get(f"http://votre_site.com/random-cat?api_key={api_key}")
        if response.status_code == 200:
            image_url = response.json()['image_url']
            await message.channel.send(image_url)
        else:
            await message.channel.send("API key is invalid or other error occurred.")

client.run('votre_token_bot_discord')
