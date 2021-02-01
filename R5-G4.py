import discord
from discord.ext import commands
import random
import os
import time

RES_DIR = os.path.dirname(os.path.abspath(__file__)) + "/res/"

print("Vwooooo!")

R5 = commands.Bot(command_prefix='R5:')

channelSounds = ['vc1.mp3', 'vc2.mp3', 'vc3.mp3']
randomSounds = ['r1.mp3', 'r2.mp3', 'r3.mp3', 'r4.mp3', 'r5.mp3', 'r6.mp3', 'r7.mp3', 'r8.mp3']
err = 'err.mp3'


def returnChannelSound():
    clip = channelSounds[random.randint(0, 2)]
    print(clip)
    return RES_DIR + clip


def returnRandomSound():
    return RES_DIR + randomSounds[random.randint(0, 7)]


@R5.command('obligation')
async def obligation(ctx):
    voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
    try:
        voice.play(discord.FFmpegPCMAudio(returnRandomSound()))
        await ctx.send(random.randint(1, 100))
    except discord.ext.commands.CommandInvokeError:
        await ctx.send(random.randint(1, 100))



@R5.command('join')
async def join(ctx):
    vc = ctx.message.author.voice.channel
    try:
        await vc.connect()
        voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(returnChannelSound()))
    except discord.ClientException:
        voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
        await ctx.send("BEEEEP!")
        voice.play(discord.FFmpegPCMAudio(RES_DIR + err))


@R5.command('leave')
async def leave(ctx):
    try:
        R5.voice_clients[0].play(discord.FFmpegPCMAudio(returnChannelSound()))
        print("snooze")
        time.sleep(4)
        await R5.voice_clients[0].disconnect()
    except discord.ClientException:
        await ctx.send("BEEEEP!")
    except IndexError:
        await ctx.send("BEEEEP!")
    finally:
        print("Sound played")


@R5.command('play')
async def play(ctx, song: str):
    voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(song))


@R5.command('stop')
async def stop(ctx):
    voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
    voice.stop()


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


R5.run("")
