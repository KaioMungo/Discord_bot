import discord
from discord.ext import commands, tasks

class Eventos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.enviar_mensagem.start()
        self.enviar_lembrete.start()

    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        if msg.author.bot:
            return
        await self.bot.process_commands(msg)

    @commands.Cog.listener()
    async def on_member_join(self, membro: discord.Member):
        canal = self.bot.get_channel(1376919442499309671)
        await canal.send(f'{membro.mention} entrou no servidor')

        embed_membro = discord.Embed(
            title=f"Membro {membro.name} acaba de entrar no servidor",
            color=discord.Color.dark_orange()
        )
        imagem = discord.File('img/saudacoes.png', 'img/saudacoes.png')
        embed_membro.set_image(url='attachment://saudacoes.png')
        embed_membro.add_field(name='Status: ', value=f'{membro.name} entrou há poucos segundos', inline=True)
        embed_membro.set_footer(text='Estamos felizes em te receber!')

        await canal.send(embed=embed_membro, file=imagem)

    @commands.Cog.listener()
    async def on_reaction_add(self, reacao: discord.Reaction, membro: discord.Member):
        await reacao.message.reply(f'O membro {membro.name} reagiu à mensagem com {reacao.emoji}')

    @tasks.loop(hours=1)
    async def enviar_mensagem(self):
        canal = self.bot.get_channel(1376919442499309671)
        await canal.send("Sou o Bot Teixeira, seu companheiro!")

    @tasks.loop(minutes=50)
    async def enviar_lembrete(self):
        canal = self.bot.get_channel(1376919442499309671)
        await canal.send("Digite [.falar_comandos] para mostrar os comandos disponíveis")

async def setup(bot):
    await bot.add_cog(Eventos(bot))
