import discord
from discord.ext import commands
import random
import praw

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.dm_messages = True

#Reddit application information, needed for some commands to run
reddit = praw.Reddit( 
    client_id = "",
    client_secret ="",
    username ="",
    password = "",
    user_agent = "",
    check_for_async = False
)
    
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

#----------------------Bot Commands-------------------------------------

@client.command()
async def letter(ctx, channel_id):
    channel = client.get_channel(int(channel_id))
    await ctx.send("guh???")
    letter = await client.wait_for("message")
    await channel.send(f"{letter.content}")

@client.command()
async def meoow(ctx, member: discord.Member):
    await ctx.send("meow?")
    try:
        message = await client.wait_for("message", check=lambda m: m.author.id == ctx.author.id, timeout=60)
        await member.send(f"{message.content}")
    except asyncio.TimeoutError:
        await ctx.send("No response received. Timeout reached.")

@client.command()#- Purge previous messages
async def purge(ctx, amount : int):
    channel = ctx.channel
    await channel.purge(limit = amount + 1)
	
@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("comedyheaven")
    hot = subreddit.hot(limit = 10)
    all_posts = []

    for post in hot:
        all_posts.append(post)
    
    random_post = random.choice(all_posts)

    PostTitle =  random_post.title
    url = random_post.url
    em = discord.Embed(title = PostTitle)
    em.set_image(url = url)
    await ctx.send(embed = em)

@client.command()
async def send_message(ctx):
    UserID = input("Please Enter Use ID: ")
    Message = input("Enter your message: ")

    try:
        user = await client.fetch_user(int(UserID))
        await user.send(Message)
        print(f"Message successfully sent to {UserID}")
    except discord.NotFound:
        print(f"User not found")
    except discord.HTTPException: 
        print(f"Failed to sent message")

@client.command()   
async def RAH(ctx, UserID:discord.Member, des):
    FingerList= ["https://tenor.com/view/fun-middle-finger-selfie-gif-13589115",
                 "https://cdn.discordapp.com/attachments/1112848103574360095/1118303088776859749/images.png",
                 "https://tenor.com/view/bocchi-the-rock-kita-the-rock-gif-27462712"]
    await ctx.message.delete()
    await ctx.channel.send(f"{ctx.author.mention} says Fuck You {UserID.mention}\n{random.choice(FingerList)}")	

@client.command() #Relocate specific user to another channel    
async def shoo(ctx, UserID:discord.Member, destination_channel:int):
    destination_channel = client.get_channel(destination_channel)
    await UserID.move_to(destination_channel)

#----------------------Bot Listeners-------------------------------------
	
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
        496892287473680384: ["Prince Smells","Prince does not own Windows"], 
        510637211612479489: ["Steven Hem Chheng does not own a house", "Mongolian"],
        337091661228408835: ["hahrahr your mother","White Cat should be CEO", "https://media.discordapp.net/attachments/960353238354386975/1109494517280808981/Baked.gif"],
        288186865411031040: ["https://media.discordapp.net/attachments/960353238354386975/1109494517280808981/Baked.gif","https://tenor.com/view/bellebows-tiktok-dog-funny-silly-gif-26293491"]
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

@client.event
async def on_voice_state_update(member,before ,after):
    target_user_id = 496892287473680384  #specific user
    destination_channel_id = 815079426684878848  # the destination channel
    sc= before
    if member.id == target_user_id and after.channel != client.get_channel(destination_channel_id):
        destination_channel = client.get_channel(destination_channel_id)
        await member.move_to(destination_channel)


client.run("")
