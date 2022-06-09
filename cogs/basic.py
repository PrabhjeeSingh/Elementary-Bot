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

    # Command to Kick people
    @commands.command()
    # Making command only accessible to administrator 
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member:discord.Member):
        await member.kick()
        await ctx.send(f"{member.name} has been kicked by {ctx.author.name}!")
        # await ctx.message.add_reaction(":poop:")
       
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member:discord.Member, reason ="I don't like him"):
        await member.ban()
        await ctx.send(f'{member.name} has been banned because {reason}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx,member):
        # getting all banned users in the guild
        banned= await ctx.guild.bans()
        name,id=member.split('#')
        # Loop for going through the banned user and comparing with  
        for ban_entry in banned:
            user = ban_entry.user
            if(user.name, user.discriminator)==(name,id):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.name} has been unbanned because I am feeling good')





# Method to make an object of this class 
# Setup method will be called when running this file
# client is accessed from the main.py
# add_cog is the function to add this particular class to cog list


def setup(client):
    client.add_cog(Basic(client))









