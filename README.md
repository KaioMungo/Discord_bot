📚 README.md – Bot Teixeira
🤖 Sobre o Projeto
O Bot Teixeira é um bot de Discord desenvolvido com a biblioteca discord.py que oferece diversas funcionalidades, como:

Mensagens de boas-vindas

Comandos matemáticos

Consultar o clima de uma cidade

Reações interativas

Envio de embeds personalizados

Mensagens automáticas com tasks.loop

Este projeto é ideal para quem quer aprender a modularizar bots em Python usando Cogs.

⚙️ Tecnologias Utilizadas
Python 3.11

discord.py

python-dotenv

requests

OpenWeather API

📂 Estrutura de Pastas
text
Copiar
Editar
meu_bot/
│
├── main.py              # Arquivo principal - executa o bot
├── .env                 # Arquivo dos tokens e chaves - protegido
├── .gitignore           # Arquivos ignorados pelo Git
├── requirements.txt     # Bibliotecas utilizadas
└── cogs/                # Comandos separados por arquivos
    ├── eventos.py       # Eventos do bot (mensagens, boas-vindas, tasks)
    ├── comandos.py      # Comandos matemáticos e utilitários
    └── tempo.py         # Comando de clima

🚀 Como Rodar o Projeto
Clone o repositório:


git clone https://github.com/KaioMungo/Discord_bot.git
Instale as dependências:

pip install -r requirements.txt
Crie um arquivo .env e adicione:


BOT_TOKEN=seu_token_do_bot
API_KEY_WEATHER=sua_chave_da_api
Execute o bot:


python main.py
📜 Lista de Comandos
📌 Comandos Básicos:
Comando	Descrição
.ola	Cumprimenta o usuário
.falar_comandos	Lista os comandos disponíveis
.falar <mensagem>	O bot repete a mensagem enviada

🧮 Comandos Matemáticos:
Comando	Descrição
.somar <n1> <n2>	Soma dois números
.subtrair <n1> <n2>	Subtrai dois números
.multiplicar <n1> <n2>	Multiplica dois números
.dividir <n1> <n2>	Divide dois números
.potencia <n1> <n2>	Calcula potência

🎮 Comandos Extras:
Comando	Descrição
.jogar_moeda <cara ou coroa>	Jogo de cara ou coroa
.info_usuario [@user]	Exibe informações de um usuário
.tempo <cidade>	Mostra o clima da cidade
.saopaulo	Exibe informações sobre o São Paulo FC
.enviar_embed	Envia uma embed personalizada

🎉 Funcionalidades Automáticas:
✅ Mensagem de boas-vindas no canal ao entrar no servidor

✅ Envio de embed personalizada na entrada

✅ Mensagens automáticas com tasks.loop:

A cada 1 hora: Mensagem padrão

A cada 50 minutos: Lembrete dos comandos

🔗 API Utilizada
OpenWeatherMap – Consultas de clima em tempo real