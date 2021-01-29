import discord
from discord.ext import commands
import random

print("Vwooooo!")

R5 = commands.Bot(command_prefix='R5:')


@R5.command('obligation')
async def obligation(ctx):
    await ctx.channel.send(str(random.randint(1, 100)))


@R5.command('join')
async def join(ctx):
    vc = ctx.message.author.voice.channel
    try:
        await vc.connect()
    except discord.ClientException:
        await ctx.send("BEEEEP!")


@R5.command('leave')
async def leave(ctx):
    try:
        await R5.voice_clients[0].disconnect()
    except discord.ClientException:
        await ctx.send("BEEEEP!")
    except IndexError:
        await ctx.send("BEEEEP!")


@R5.command('play')
async def play(ctx, song: str):
    voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(song))


# @R5.command('pause')
# async def pause(ctx):
#     voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
#     if voice.is_playing():
#
#     else:
#         await ctx.send("BEEEEP!")
#
# @R5.command('resume')
# async def resume(ctx):
#     voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
#     if voice.is_paused():
#         voice.resume
#     else:
#         await ctx.send("BEEEEP!")
#
# @R5.command('stop')
# async def stop(ctx):
#     voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
#     voice.stop()


R5.run("")
