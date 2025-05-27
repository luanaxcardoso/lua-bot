1. Crie um bot no Discord Developer Portal
Vá para: https://discord.com/developers/applications

Clique em "New Application"

Dê um nome (ex: MeuBot)

Vá em "Bot" > "Add Bot" > Yes, do it!

Em "Bot", ative:

"MESSAGE CONTENT INTENT"

"SERVER MEMBERS INTENT" (opcional)

Copie o Token do Bot (vamos usar no código)

⚠️ Guarde o token com segurança. Nunca publique em repositórios.

2. Crie um servidor no Discord e convide o bot para seu servidor

3. Volte ao Discord Developer Portal
Vá para: https://discord.com/developers/applications

Vá em "OAuth2 > URL Generator"

Marque:

SCOPES: bot

BOT PERMISSIONS: Send Messages, Read Message History, View Channels

e de permissões de administrador
Clique em "Copy" para copiar a URL gerada
Copie a URL gerada e abra no navegador

Selecione seu servidor e autorize

3. Crie o arquivo do bot.py
Crie um arquivo .env na mesma pasta do bot.py e adicione o token do bot:

4. Instale as dependências necessárias de requirements.txt

```bash
pip install -r requirements.txt

```

1. 🌙 Comandos da Lua Bot

- `!hello` 👋  
  Receba uma saudação da Lua Bot.

- `!info` ℹ️  
  Veja informações sobre o bot.

- `!ajuda` 📜  
  Exibe esta mensagem de ajuda.

- `!piada` 😂  
  Conte uma piada aleatória.

- `!hora` ⏰  
  Mostra a hora atual.

- `!lua` 🌙  
  Envia uma mensagem especial com emoji da Lua.

- `!curtir` 👍  
  Reage com 👍 à sua mensagem.

- `!sobre` 🔮  
  Informações adicionais sobre a Lua Bot.
