import discord
from discord.ext import commands
from config import settings

intents = discord.Intents.default()

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)

@bot.event
async def on_member_join(member):
    invites_before_join = await member.guild.invites()
    user_invites_before_join = {invite.code: invite for invite in invites_before_join}
    invites_after_join = await member.guild.invites()
    for invite in invites_after_join:
        if invite.uses > user_invites_before_join[invite.code].uses:
            channel = bot.get_channel(1209811462093152289)
            await channel.send(f"{member.name} присоединился, используя приглашение от {invite.inviter.name}")
            break

bot.run(settings['token'])