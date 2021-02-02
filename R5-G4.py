import os
import random
import time

import discord
from discord.ext import commands

RES_DIR = os.path.dirname(os.path.abspath(__file__)) + "/res/"


print("Vwooooo!")

R5 = commands.Bot(command_prefix='R5:')

channelSounds = ['vc1.mp3', 'vc2.mp3', 'vc3.mp3']
randomSounds = ['r1.mp3', 'r2.mp3', 'r3.mp3', 'r4.mp3', 'r5.mp3', 'r6.mp3', 'r7.mp3', 'r8.mp3']
err = 'err.mp3'


def returnChannelSound():
    return RES_DIR + channelSounds[random.randint(0, 2)]


def returnRandomSound():
    return RES_DIR + randomSounds[random.randint(0, 7)]


@R5.command('speak', brief="R5 plays a random sound")
async def speak(ctx):
    R5.voice_clients[0].play(discord.FFmpegPCMAudio(returnRandomSound()))


@R5.command('obligation', brief="R5 rolls a d100 to determine the obligation.")
async def obligation(ctx):
    voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
    try:
        voice.stop()
        voice.play(discord.FFmpegPCMAudio(returnRandomSound()))
        await ctx.send(random.randint(1, 100))
    except discord.ext.commands.CommandInvokeError:
        await ctx.send(random.randint(1, 100))
    except AttributeError:
        await ctx.send(random.randint(1, 100))


@R5.command('join', brief="Joins R5 to the voice channel.")
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


@R5.command('leave', brief="Kicks R5 from the voice channel.")
async def leave(ctx):
    try:
        R5.voice_clients[0].stop()
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


@R5.command('play', brief="Plays a song that R5 has in his memory banks")
async def play(ctx, song: str):
    voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(song))


@R5.command('stop', brief="Stops R5 from playing any music.")
async def stop(ctx):
    voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
    voice.stop()


@R5.command('query', brief='Search databank for information about a subject. Encase in ""')
async def query(ctx, arg: str):
    userquery = arg.replace('"', '').replace(" ", "_")
    await ctx.message.author.send("https://starwars.fandom.com/wiki/" + userquery)


R5.run("")
