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

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    Remessages = message.content.lower() #Will check all messages in lowercase

    if Remessages == "meow":
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

    for word in messages.split():
         if word in check_messages:
            await message.channel.send(check_messages[word])
            break

    await client.process_commands(message)


client.run("")
