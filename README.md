# 🌙 Lua Bot

Um bot para Discord feito em Python.

## Sumário

- [🌙 Lua Bot](#-lua-bot)
  - [Sumário](#sumário)
  - [Visão Geral](#visão-geral)
  - [Pré-requisitos](#pré-requisitos)
  - [Configuração](#configuração)
    - [1. Crie um Bot no Discord Developer Portal](#1-crie-um-bot-no-discord-developer-portal)
  - [2. Convidar o Bot para Seu Servidor](#2-convidar-o-bot-para-seu-servidor)

---

## Visão Geral

Lua Bot é um bot para Discord que foi criado para ajudar e interagir com os usuários por meio de comandos simples, como `!hello`, `!piada`, `!hora` e outros. O projeto utiliza a biblioteca [discord.py](https://discordpy.readthedocs.io/en/stable/) e a [python-dotenv](https://pypi.org/project/python-dotenv/) para carregar variáveis de ambiente.

---

## Pré-requisitos

- Python 3.8 ou superior
- Uma conta no Discord
- Acesso ao [Discord Developer Portal](https://discord.com/developers/applications)

---

## Configuração

### 1. Crie um Bot no Discord Developer Portal

1. Acesse: [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em **"New Application"**.
3. Dê um nome para sua aplicação (ex: `Lua Bot 🌙`).
4. No menu lateral, clique em **"Bot"** e depois em **"Add Bot"**. Confirme a ação com **"Yes, do it!"**.
5. Em **Privileged Gateway Intents**, ative:
   - **MESSAGE CONTENT INTENT** (obrigatório para ler mensagens)
   - **SERVER MEMBERS INTENT** (opcional, se precisar de informações dos membros)
6. Copie o **Token do Bot**. **⚠️ Importante:** Nunca compartilhe seu token publicamente, pois ele permite o controle total do bot.
7. Guarde o token em um arquivo chamado `.env` (na raiz do projeto), conforme o exemplo abaixo:

## 2. Convidar o Bot para Seu Servidor

1. No [Discord Developer Portal](https://discord.com/developers/applications), vá até a aba **OAuth2 > URL Generator**.

2. Em **SCOPES**, marque a opção:
   - `bot`

3. Em **BOT PERMISSIONS**, selecione as permissões desejadas:
   - `Send Messages`
   - `Read Message History`
   - `View Channels`
   - *(Opcional)* `Administrator` — se quiser conceder permissões totais ao bot

4. Copie a **URL gerada** ao final da página.

5. Abra essa URL no Discord no servidor onde deseja adicionar o bot.

6. Escolha o servidor em que deseja adicionar o bot e clique em **"Autorizar"**.

7. Rode o bot localmente com o comando:

```bash
python bot.py
```

8. Verifique se o bot está online no seu servidor Discord.
9. Teste os comandos disponíveis, como `!hello`, `!piada`, `!hora`, etc.

✅ Pronto! O bot agora estará no seu servidor e pronto para ser usado.
