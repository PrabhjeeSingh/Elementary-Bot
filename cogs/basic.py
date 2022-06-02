import discord
from discord.ext import commands

print("Reached")
# Creating a class and its methods
# Capital B naming convention
class Basic(commands.Cog):
    # Mandatory Constructors take client as a parameter
    def __init__(self,client):
        self.client=client
     
    
    """ Events """
    # Now commonds.Cog.listener is a decorator to add a event function to our Bot program 
    @commands.Cog.listener()
    async def on_ready(self):
        # await ctx.send("I am back baby")
        print("Baby is up :)")

    """ commands """
    # commands.command is the decorator to
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"Pong {round(self.client.latency*1000)}ms")


    


# Method to make an object of this class 
# Setup method will be called when running this file
# client is accessed from the main.py
# add_cog is the function to add this particular class to cog list


def setup(client):
    client.add_cog(Basic(client))









