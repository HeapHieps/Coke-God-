import discord
from discord.ext import commands

#intents = discord.Intents.default()
#intents.message_content = True

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.command()
async def ping(ctx,arg):
    await ctx.send(arg)

@client.command()
async def meoow(ctx,member:discord.Member):
	await ctx.send("meow?")
	def check(m):
		return m.author.id == ctx.author.id
	message = await client.wait_for("message", check = check)
	await member.send(f"{message.content}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "meow":
        await message.channel.send("Meow")
    
    author_messages = {
        496892287473680384: "Prince Smells", 
        510637211612479489: "Steven Hem Chheng does not own a house" 
    }

    if message.author.id == author_messages:
        reactions = ["⏸️", "🇴", "💀", "🇼", "🇮", "🇳", "🇩", "🅾️", "🪟"]
    for reaction in reactions:
        await message.add_reaction(reaction)
    await client.process_commands (message)
    
    if message.author.id in author_messages:
        await message.channel.send(author_messages[message.author.id])

client.run("")
