### how to run 

1. **download repository**
go [here](https://github.com/settings/tokens/new) choose `repo` in scopes and generate token
use `git clone https://<token>@github.com/<your username>/nekki_discord_bot.git` to clone
2. **configure your config file**
```
settings = {
    'token': 'Bot token here',
    'bot': 'Bot name here',
    'id': bot_app_id_here
}
```
you can create your bot at [discord developer portal](https://discord.com/developers/applications/)
3. **set channel ID**
https://github.com/muhyrla/nekki_discord_bot/blob/bb998bcf1b62c971b68f8b36d8b3b2661dcd33b8/button.py#L65
4. **download dependencies**
`pip install disnake`

------------