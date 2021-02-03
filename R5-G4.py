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
    return RES_DIR + 'vcSounds/' + channelSounds[random.randint(0, 2)]


def returnRandomSound():
    return RES_DIR + 'rSounds/' + randomSounds[random.randint(0, 7)]


def returnAtmosphericSound(arg: str):
    return RES_DIR + 'atmosSounds/' + arg + '.mp3'


@R5.command('speak', brief="*R5 plays a random sound")
async def speak(ctx):
    R5.voice_clients[0].play(discord.FFmpegPCMAudio(returnRandomSound()))


@R5.command('obligation', brief="R5 rolls a d100 to determine the obligation.")
async def obligation(ctx):
    try:
        if not R5.voice_clients[0].is_playing():
            R5.voice_clients[0].play(discord.FFmpegPCMAudio(returnRandomSound()))
            await ctx.send(random.randint(1, 100))
        else:
            await ctx.send(random.randint(1, 100))
    except discord.ext.commands.CommandInvokeError:
        await ctx.send(random.randint(1, 100))
    except AttributeError:
        await ctx.send(random.randint(1, 100))


@R5.command('join', brief="Joins R5 to the voice channel. * means voice only!")
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


@R5.command('leave', brief="*Kicks R5 from the voice channel.")
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


@R5.command('play', brief="*Plays a song that R5 has in his memory banks")
async def play(ctx, song: str):
    voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(song))


@R5.command('stop', brief="*Stops R5 from playing any music/sounds.")
async def stop(ctx):
    voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
    voice.stop()


@R5.command('query', brief='Search databank for information about a subject. Encase in ""')
async def query(ctx, arg: str):
    userquery = arg.replace('"', '').replace(" ", "_")
    try:
        if not R5.voice_clients[0].is_playing:
            R5.voice_clients[0].play(discord.FFmpegPCMAudio(returnRandomSound()))
            await ctx.message.author.send("https://starwars.fandom.com/wiki/" + userquery)
        else:
            await ctx.message.author.send("https://starwars.fandom.com/wiki/" + userquery)
    except discord.ext.commands.CommandInvokeError:
        await ctx.message.author.send("https://starwars.fandom.com/wiki/" + userquery)
    except AttributeError:
        await ctx.message.author.send("https://starwars.fandom.com/wiki/" + userquery)


@R5.command('atmos', brief='*Plays atmospheric sounds. R5:help atmos to get list of sounds',
            description="List of sound options will be here")
async def query(ctx, arg: str):
    R5.voice_clients[0].play(discord.FFmpegPCMAudio(returnAtmosphericSound(arg)))


R5.run("")


"Player Handbook can be downloaded here:"
"https://drive.google.com/file/d/1etmm_GumqWdRdmlRZBA2hEGKR2sadT-G/view?usp=sharing"

"Free App for Dice for Cheap Ass Folks:"
"https://play.google.com/store/apps/details?id=com.visttux.empireedgediceroller&hl=en_US&gl=US"

"Guide for people who can't read (Like me)"
"https://www.youtube.com/watch?v=Ht6x47NhgG8"