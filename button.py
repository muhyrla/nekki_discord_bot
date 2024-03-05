import sqlite3
from config import settings
import disnake
from disnake.ext import commands
from disnake import TextInputStyle, ButtonStyle, ui

bot = commands.Bot(command_prefix="")
conn = sqlite3.connect('player_ids.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS players
             (discord_username text, discord_id text, player_id text)''')


class MyButton(ui.Button):
    def __init__(self):
        super().__init__(style=ButtonStyle.primary, label="Submit Player ID")

    async def callback(self, inter: disnake.Interaction):
        c.execute("SELECT * FROM players WHERE discord_id = ?", (str(inter.user.id),))
        data = c.fetchone()
        if data is not None:
            await inter.response.send_message("You have already submitted your Player ID.", ephemeral=True)
        else:
            await inter.response.send_modal(modal=MyModal())


class MyModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Player ID",
                placeholder="Enter your ID here.",
                custom_id="player_id",
                style=TextInputStyle.short,
                max_length=50,
            ),
        ]
        super().__init__(title="Enter your Player ID here.", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        player_id = inter.text_values["player_id"]
        if not player_id.isdigit():
            await inter.response.send_message("Player ID should consist only from digits.", ephemeral=True)
            return
        c.execute("INSERT INTO players VALUES (?, ?, ?)", (str(inter.user), str(inter.user.id), player_id))
        conn.commit()
        embed = disnake.Embed(title="Player ID")
        embed.add_field(
            name="Player ID",
            value=player_id,
            inline=False,
        )
        print(f'Got new ID: {player_id}')
        await inter.response.send_message(f'Thank you!\n\nYou successfully submitted:\nPlayer ID: {player_id}\n\nWe will issue the armor soon.', ephemeral=True)


class MyView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(MyButton())


@bot.event
async def on_ready():
    channel = bot.get_channel() # put channel ID in brackets
    if channel is not None:
        await channel.send("Press the button below to submit your ID.", view=MyView()) # You can edit message text here
    else:
        pass


bot.run(settings['token'])
