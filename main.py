from errno import EXDEV
import discord
from discord.ext import commands
import os



client = commands.Bot("!")



# Client is the class
# @ client.command is the decorator which is adding followinf function to already created client class

# @client.event
# async def on_ready():
#     # client.send("I'm Back")
#     print("Baby is up : )")


channel_list=[]
print(list(client.get_all_channels()))


"""Method to Load cogs pages"""
# ctx = client class object which store basic functionality
##### DO Not change 'ctx' to anything it's a keyword #####
# extension = name of the cogs page to load
@client.command()
@commands.has_any_role("Managers","Founders")
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"{extension} was loaded.")


# UnLoad command to unload a python page
@client.command()
@commands.has_any_role("Managers","Founders")
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"{extension} was unloaded.")

@client.command()
@commands.has_any_role("Managers","Founders")
async def reload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f"{extension} reload complete")
    except Exception:
        await ctx.send(Exception)

# Loading all cogs during start of the program
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(filename)


#Bot token: and event looop 
client.run("OTgxOTcyNjUzNzg1MDg4MDEw.GS_ewu.L1M0vr3O1nY_70ZWKw1Vw2NAeB2m2xSUqWxyjQ")












