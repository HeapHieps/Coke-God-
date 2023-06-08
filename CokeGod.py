import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.dm_messages = True


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.command()
async def ping(ctx, arg):
    await ctx.send(arg)

@client.command()
async def meoow(ctx, member: discord.Member):
	await ctx.send("meow?")
	def check(m):
		return m.author.id == ctx.author.id

	message = await client.wait_for("message", check = check)
	await member.send(f"{message.content}")
        
@client.command()
async def send_message(ctx):
    UserID = input("Please Enter Use ID: ")
    Message = input("Enter your message: ")
    user = await client.fetch_user(int(UserID))
    await user.send(Message)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    ReMessage = message.content.lower() #Will check all messages in lowercase

    if ReMessage == "meow":
        await message.channel.send("Meow")

    if message.author.id == 496892287473680384:
        reactions = ["⏸️", "🇴", "💀", "🇼", "🇮", "🇳", "🇩", "🅾️", "🪟"]
        for reaction in reactions:
            await message.add_reaction(reaction)
    
    author_messages = {
        496892287473680384: ["Prince Smells","Prince does not own Window"], 
        510637211612479489: ["Steven Hem Chheng does not own a house", "Mongolian"], 
        337091661228408835: ["hahrahr your mother","White Cat should be CEO"], 
    }

    check_messages = {
        "ceo":"White Cat CEO",
        "har":"Harharharh"
    }

    if message.author.id in author_messages:
        messages = author_messages[message.author.id]
        selected_message = random.choice(messages)
        await message.channel.send(selected_message)

    for word in ReMessage.split():
        if word in check_messages:
            await message.channel.send(check_messages[word])
            break 

    if isinstance(message.channel, discord.DMChannel): #Receive any incoming DMs and prints the contents in console  
        print(f"{message.author}: {message.content}")

    await client.process_commands(message)


client.run("")
