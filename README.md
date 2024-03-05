<br/>
<p align="center">
  <a href="https://github.com/muhyrla/nekki_discord_bot">
    <img src="https://i.playground.ru/p/L6ZtHmA6a-Tux_VBpWx7gQ.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Discord button-bot</h3>

</p>



## Built With

**Python 3.12.1**

https://github.com/DisnakeDev/disnake

## Getting Started

Before all, you need to create your bot at [Discord developer portal](https://discord.com/developers/applications/).

### Prerequisites

You need only one lib

* disnake

```sh
pip install disnake
```

### Installation

1. Create your GitHub PAT.

**[here](https://github.com/settings/tokens/new)** choose `repo` in scopes and generate token.

2. Clone the repo.

```sh
git clone https://<token>@github.com/<your username>/nekki_discord_bot.git
```

3. Install prerequisites.

```sh
pip install disnake
```

4. Enter your data in `config.py`

```python
settings = {
    'token': 'Bot token here',
    'bot': 'Bot name here',
    'id': bot_app_id_here,
    'channel_id': channel_id
}
```
--------------
