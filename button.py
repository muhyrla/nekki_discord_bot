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
        super().__init__(style=ButtonStyle.primary, label="Submit Player ID") # text ON the buttonm

    async def callback(self, inter: disnake.Interaction):
        c.execute("SELECT * FROM players WHERE discord_id = ?", (str(inter.user.id),))
        data = c.fetchone()
        if data is not None:
            await inter.response.send_message("You have already submitted your Player ID.", ephemeral=True) # text if someonwe trys to submit more then one time
        else:
            await inter.response.send_modal(modal=MyModal())


class MyModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Player ID",                      # text above text field
                placeholder="Enter your ID here.",      # text in text field
                custom_id="player_id",                  # dont touch
                style=TextInputStyle.short,
                max_length=50,
            ),
        ]
        super().__init__(title="Enter your Player ID here.", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        player_id = inter.text_values["player_id"]
        if not player_id.isdigit():
            await inter.response.send_message("Player ID should consist only from digits.", ephemeral=True) # text if player ID consists NOT only of digits
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
        await inter.response.send_message(f'Thank you!\n\nYou successfully submitted:\nPlayer ID: {player_id}\n\nWe will issue the armor soon.', ephemeral=True) # text after good submit


class MyView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(MyButton())


@bot.event
async def on_ready():
    channel = bot.get_channel(settings['channel_id'])
    if channel is not None:
        await channel.send("Press the button below to submit your ID.", view=MyView()) # message text 
    else:
        pass


bot.run(settings['token'])
