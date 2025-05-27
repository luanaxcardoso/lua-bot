import discord  # type: ignore
import os
import random
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bot_name = "Lua Bot 🌙"
        self.description = "Sou uma bot feita para ajudar e iluminar seu servidor!"
        self.version = "1.0"
        self.jokes = [
            "Por que o computador foi ao médico? Porque estava com um vírus! 🤒",
            "O que o Java disse para o Python? Você é tão dinâmico! 🐍",
            "Por que o programador sempre confunde Halloween e Natal? Porque OCT 31 == DEC 25! 🎃🎄"
        ]

    async def on_ready(self):
        print(f'✅ Logado como {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author == self.user:
            return

        content = message.content.lower()

        if content.startswith('!hello'):
            await message.channel.send(f'Olá {message.author.mention}! Eu sou a {self.bot_name}.')

        elif content.startswith('!ajuda'):
            embed = discord.Embed(
                title="📜 Comandos disponíveis",
                description="Aqui estão alguns comandos que você pode usar:",
                color=discord.Color.purple()
            )
            embed.add_field(name="!hello", value="Receba uma saudação da Lua Bot.", inline=False)
            embed.add_field(name="!info", value="Veja informações sobre mim.", inline=False)
            embed.add_field(name="!ajuda", value="Exibe esta mensagem de ajuda.", inline=False)
            embed.add_field(name="!piada", value="Conte uma piada aleatória. 😂", inline=False)
            embed.add_field(name="!hora", value="Mostra a hora atual. ⏰", inline=False)
            embed.add_field(name="!lua", value="Mensagem e emoji da Lua. 🌙", inline=False)
            embed.add_field(name="!curtir", value="Reage com 👍 à sua mensagem.", inline=False)
            embed.add_field(name="!sobre", value="Informações sobre a Lua Bot. 🔮", inline=False)
            await message.channel.send(embed=embed)

        elif content.startswith('!info'):
            embed = discord.Embed(
                title=self.bot_name,
                description=self.description,
                color=discord.Color.blurple()
            )
            embed.add_field(name="Versão", value=self.version)
            embed.set_footer(text="Feito com 💙 usando discord.py")
            await message.channel.send(embed=embed)

        elif content.startswith('!piada'):
            joke = random.choice(self.jokes)
            await message.channel.send(joke)

        elif content.startswith('!hora'):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            await message.channel.send(f"A hora atual é: ⏰ {current_time}")

        elif content.startswith('!lua'):
            await message.channel.send("Aqui está a Lua para você! 🌖✨")
            await message.add_reaction("🌙")

        elif content.startswith('!curtir'):
            await message.add_reaction('👍')

        elif content.startswith('!sobre'):
            embed = discord.Embed(
                title="🔮 Sobre a Lua Bot 🌙",
                description="Eu ilumino o seu servidor com ajuda e diversão!",
                color=discord.Color.dark_blue()
            )
            embed.set_footer(text="Feito por Luana 🌙")
            await message.channel.send(embed=embed)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
