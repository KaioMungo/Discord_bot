import discord
from discord.ext import commands
import random

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ola(self, ctx: commands.Context):
        nome = ctx.author.name
        await ctx.reply(f'Olá, {nome}! Tudo bem?')

    @commands.command()
    async def falar_comandos(self, ctx: commands.Context):
        texto = "Lista de comandos: .ola | .falar (texto) | .somar (numeros) | .subtrair (numeros) | .multiplicar (numeros) | .dividir (numeros) | .potencia (numeros) | .enviar_embed | .info_usuario (usuario) | .jogar_moeda (cara ou coroa) | .tempo (cidade) | .saopaulo | ou até mesmo digitando ['/']"
        await ctx.send(texto)

    @commands.command()
    async def falar(self, ctx: commands.Context, *, texto):
        await ctx.send(texto)

    @commands.command()
    async def somar(self, ctx: commands.Context, num1: float, num2: float):
        resultado = num1 + num2
        await ctx.reply(f'A soma entre {num1} + {num2} é igual a {resultado}')

    @commands.command()
    async def subtrair(self, ctx: commands.Context, num1: float, num2: float):
        resultado = num1 - num2
        await ctx.reply(f'A subtração entre {num1} e {num2} é igual a {resultado}')

    @commands.command()
    async def multiplicar(self, ctx: commands.Context, num1: float, num2: float):
        resultado = num1 * num2
        await ctx.reply(f'A multiplicação entre {num1} e {num2} é igual a {resultado}')

    @commands.command()
    async def dividir(self, ctx: commands.Context, num1: float, num2: float):
        resultado = num1 / num2
        await ctx.reply(f'A divisão entre {num1} e {num2} é igual a {resultado}')

    @commands.command()
    async def potencia(self, ctx: commands.Context, num1: float, num2: float):
        resultado = num1 ** num2
        await ctx.reply(f'O {num1} elevado a {num2} é igual a {resultado}')

    @commands.command()
    async def jogar_moeda(self, ctx: commands.Context, escolha):
        escolha = escolha.lower()
        resultado = random.choice(['cara', 'coroa'])
        if escolha == resultado:
            await ctx.send(f"{ctx.author.name} acertou! Deu {resultado}!")
        else:
            await ctx.send(f"{ctx.author.name} errou! Deu {resultado}!")

    @commands.command()
    async def info_usuario(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        embed = discord.Embed(
            title=f"Informações de {member}",
            color=discord.Color.blue(),
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.add_field(name="Nome", value=member.name, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Entrou no servidor", value=member.joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Criou a conta em", value=member.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Status", value=str(member.status).title(), inline=True)
        embed.add_field(name="Cargo mais alto", value=member.top_role.mention, inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def enviar_embed(self, ctx: commands.Context):
        minha_embed = discord.Embed()
        minha_embed.title = 'Teixeira'
        minha_embed.description = 'Teixeira deixando um recado...'

        imagem = discord.File('img/jack_img.jpg', 'img/jack.jpg')
        minha_embed.set_image(url='attachment://jack.jpg')
        minha_embed.set_thumbnail(url='attachment://jack.jpg')
        minha_embed.set_footer(text='Se você não vivenciar o fracasso, não saberá reconhecer quando o sucesso realmente chegar.')
        minha_embed.set_author(name='Kaio Mungo', icon_url='https://i.pinimg.com/originals/4e/45/88/4e458893b1fdc033508016e09fa5553c.jpg', url='https://github.com/KaioMungo')

        await ctx.reply(embed=minha_embed, file=imagem)

    @commands.command()
    async def saopaulo(self, ctx: commands.Context):
        tricolor = discord.Embed(title='São Paulo FC', color=discord.Color.red())
        tricolor.set_image(url='attachment://logo-sao-paulo.png')
        tricolor.set_thumbnail(url='attachment://logo-sao-paulo.png')
        tricolor.add_field(name='Libertadores: ', value='3', inline=True)
        tricolor.add_field(name='Mundial: ', value='3', inline=True)
        tricolor.add_field(name='Brasileiro: ', value='6', inline=True)
        tricolor.add_field(name='Copa do brasil: ', value='1', inline=True)
        tricolor.add_field(name='Estádio: ', value='Morumbi', inline=True)
        tricolor.add_field(name='Quantidade de torcedores:', value='20 milhões', inline=True)
        tricolor.add_field(name='Mascote: ', value='Santo Paulo', inline=True)
        tricolor.set_author(name='Kaio Mungo', icon_url='https://http2.mlstatic.com/D_NQ_NP_687798-MLB44308479431_122020-F.jpg', url='https://www.saopaulofc.net/')

        await ctx.send(embed=tricolor)

async def setup(bot):
    await bot.add_cog(Comandos(bot))
