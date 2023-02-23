import discord, json, random, asyncio, os
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select, ButtonStyle
from discord.ext import tasks
###############################################
#               COLOR LIST                    #
orange = 0xe67e22                             #
yellow = 0xf1c40f                             #
red = 0xe74c3c                                #
dark_red = 0x992d22                           #
blue = 0x3498db                               #
###############################################
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file) # CONFIG.JSON

intents = discord.Intents.default()
client = commands.Bot(command_prefix=config['bot']['prefix'], intents=intents, case_insensitive=False) 
intents.members = True 
DiscordComponents(client) 
client.remove_command('help') 

ruleslist = """
- Be respectful, civil and welcoming.
- No racism
- Be kind and respectful to others.
- No inappropriate or dangerous content.
- Do not abuse or spam in any of the channels.
- Do not join the server to promote your content.
- Discord names and avatars must be appropriate.
- Spamming in any form is not allowed.
- No links or invitation codes to the Discord server.
- Do not advertise without permission.
- Do not link to fraudulent websites.
- Do not threaten anyone.
- Don't ask for, post or disclose hacking information, links or intentions.
- Don't post dangerous material (malicious websites, pirated software, etc.)
"""

#START UP

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="🔒 CAPTCHA Security!"))
    print(f"{client.user.name} is online.")
    print("[!] CONSOLE LOG:")
    client.loop.create_task(status_task())

# Rotating Status
async def status_task():
    while True:
         await client.change_presence(activity=discord.Game(name="🔒 CAPTCHA Security!"), status=discord.Status.online)
         await asyncio.sleep(10)
         filename = f"./database/verifycount.txt"
         with open(filename, "r") as file:
            ans = sum(int(line) for line in file)
            result = 631 + ans
            await client.change_presence(activity=discord.Game(name=f"🌐 {result} users verified in total!"), status=discord.Status.online)
         await asyncio.sleep(10)
         await client.change_presence(activity=discord.Game(name="https://www.synpy.dev/"), status=discord.Status.online)
         await asyncio.sleep(10)

@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name="❌ Unverified")
    await member.add_roles(role)

# FALSE CAPTCHA DELETE 
@client.event
async def on_message(message):
    msg_cnt = message.content.lower()
    if "!1" in msg_cnt:
        print(f'Detected false CAPTCHA "{msg_cnt}". Deleting in 10 seconds.')
        await asyncio.sleep(10)
        await message.delete()
        print("Message Deleted.")
    await client.process_commands(message)

@client.event
async def on_message(message):
    msg_cnt = message.content.lower()
    if "!2" in msg_cnt:
        print(f'Detected false CAPTCHA "{msg_cnt}". Deleting in 10 seconds.')
        await asyncio.sleep(10)
        await message.delete()
        print("Message Deleted.")
    await client.process_commands(message)

@client.event
async def on_message(message):
    msg_cnt = message.content.lower()
    if "!3" in msg_cnt:
        print(f'Detected false CAPTCHA "{msg_cnt}". Deleting in 10 seconds.')
        await asyncio.sleep(10)
        await message.delete()
        print("Message Deleted.")
    await client.process_commands(message)

@client.event
async def on_message(message):
    msg_cnt = message.content.lower()
    if "!4" in msg_cnt:
        print(f'Detected false CAPTCHA "{msg_cnt}". Deleting in 10 seconds.')
        await asyncio.sleep(10)
        await message.delete()
        print("Message Deleted.")
    await client.process_commands(message)

@client.event
async def on_message(message):
    msg_cnt = message.content.lower()
    if "!5" in msg_cnt:
        print(f'Detected false CAPTCHA "{msg_cnt}". Deleting in 10 seconds.')
        await asyncio.sleep(10)
        await message.delete()
        print("Message Deleted.")
    await client.process_commands(message)
######################################################################
# INVITE LINK DELETE
@client.event
async def on_message(message):
    msg_cnt = message.content.lower()
    user = message.author
    mutedRole = discord.utils.get(message.guild.roles, name="🚫 Muted")
    if "discord.gg" in msg_cnt:
        print(f'Detected Discord invite from "{user}". Message deleted.')
        print(f'"{user}" has been muted for 60s due to posting a Discord invite.')
        await message.delete()
        await user.add_roles(mutedRole)
        await asyncio.sleep(60)
        print(f'"{user}" Has been unmuted.')
        await user.remove_roles(mutedRole)
    await client.process_commands(message)

# COMMANDS
@client.command()
@commands.has_permissions(administrator=True)
async def safelocksetup(ctx):
    guild = ctx.guild
    await guild.create_role(name="🌟 Verified")
    await guild.create_role(name="❌ Unverified")
    await guild.create_role(name="🚫 Muted")
    mutedRole = discord.utils.get(guild.roles, name="🚫 Muted")
    Verifrole = discord.utils.get(guild.roles, name="🌟 Verified")
    await ctx.channel.purge(limit=1)
    for channel in guild.channels:
        await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        await channel.set_permissions(Verifrole, view_channel=True)
    embed = discord.Embed(title="🌟Setup Complete🌟", colour= red)
    embed.add_field(name="Role created:", value=f"🌟 Verified", inline=False)
    embed.add_field(name="Role created:", value=f"❌ Unverified", inline=False)
    embed.add_field(name="Role created:", value=f"🚫 Muted, this role is for when a user posts a Discord invite link. The message will be automatically deleted and the user will be muted for 60s.", inline=False)
    embed.set_thumbnail(url="https://i.imgur.com/PIklyu3.png")
    embed.add_field(name="Note:", value=f"When new users join the server, they will automatically be given the '❌ Unverified' role. Now you just need to run the !verify command in the channel that you want users to have to verify themselves in.", inline=False)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def verify(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="<:6375redverified:1036532239959339068> Verification Panel", colour= red)
    embed.set_thumbnail(url="https://i.imgur.com/PIklyu3.png")
    embed.add_field(name="Please read the rules before verification.", value=f"{ruleslist}", inline=False)
    embed.add_field(name="Click the button below to get verified!", value="<:reddown:1021108134267334770>", inline=False)
    await ctx.send(embed=embed, components = [
        [Button(label="Verify", style="4", emoji = "🔐", custom_id="interview")]
        ])
    while True:   
        interaction = await client.wait_for("button_click") 
        if interaction.component.label == "Verify":
            image = os.listdir('./captcha')
            imgString = random.choice(image)
            path = "./captcha/" + imgString
            embed = discord.Embed(title="Solve the captcha 🕵️", colour= red)
            embed.add_field(name="Type the CAPTCHA code with a exclaimation mark in front.", value='Example: !2gdsb', inline=False)
            embed.set_thumbnail(url="https://i.imgur.com/PIklyu3.png")
            await interaction.send(embed=embed, file=discord.File(path))
            

@client.command(name="captcha", aliases=["2bg48","22d5n","25m6p", "226md", "245y5"])
async def captcha(ctx):
        filename = f"./database/verifycount.txt"
        await ctx.channel.purge(limit=1)
        verified = discord.utils.get(ctx.guild.roles, name="🌟 Verified")
        unverified = discord.utils.get(ctx.guild.roles, name="❌ Unverified")
        await ctx.author.remove_roles(unverified)
        await ctx.author.add_roles(verified)
        embed = discord.Embed(title="<a:checkmarkoutline:1021218710884733018>  You're verified!", colour= red)
        embed.add_field(name=f"You have successfully been granted access to {ctx.guild}!", value='\u200b', inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/PIklyu3.png")
        await ctx.author.send(embed=embed)
        with open(filename, "a") as file:
                file.write("1\n")


client.run(config['bot']['token'])