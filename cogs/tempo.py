import discord
from discord.ext import commands
import requests
import os

API_KEY = os.getenv('a4f15e87b6b47b08e9489bd59ee2b3ab')

class Tempo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tempo(self, ctx, *, cidade):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric'

        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            descricao = dados['weather'][0]['description']
            temperatura = dados['main']['temp']
            sensacao = dados['main']['feels_like']
            umidade = dados['main']['humidity']

            embed = discord.Embed(title=f'Tempo em {cidade.title()}', color=discord.Color.gray())
            embed.add_field(name='Descrição', value=descricao.title(), inline=False)
            embed.add_field(name='Temperatura', value=f'{temperatura}°C', inline=True)
            embed.add_field(name='Sensação Térmica', value=f'{sensacao}°C', inline=True)
            embed.add_field(name='Umidade', value=f'{umidade}%', inline=True)

            await ctx.send(embed=embed)
        else:
            await ctx.send('Cidade não encontrada. Verifique o nome e tente novamente.')

async def setup(bot):
    await bot.add_cog(Tempo(bot))
