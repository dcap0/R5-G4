import time

import discord
from discord.ext import commands

import subsys.R5MemCalls as mem
import subsys.R5SoundCalls as snd



print("Vwooooo!")

R5 = commands.Bot(command_prefix='R5:')

#player resources
rules = "Edge of the Empire sourcebook: https://drive.google.com/file/d/1etmm_GumqWdRdmlRZBA2hEGKR2sadT-G/view?usp=sharing"
diceApp = "Android App for game dice: https://play.google.com/store/apps/details?id=com.visttux.empireedgediceroller&hl=en_US&gl=US"
videoGuide = "Quick Video Tutorial :https://www.youtube.com/watch?v=Ht6x47NhgG8"
fullResource = rules + "\n~~~~~~~~~~~~~~~~~~~~\n" + diceApp + "\n~~~~~~~~~~~~~~~~~~~~\n" + videoGuide


@R5.command('DBtest')
async def DBtest(ctx):
    await ctx.send(mem.dbtest())

@R5.command('speak', brief="*R5 plays a random sound")
async def speak(ctx):
    R5.voice_clients[0].play(discord.FFmpegPCMAudio(snd.returnRandomSound()))


@R5.command('obligation', brief="R5 rolls a d100 to determine the obligation.")
async def obligation(ctx):
    try:
        if not R5.voice_clients[0].is_playing():
            R5.voice_clients[0].play(discord.FFmpegPCMAudio(snd.returnRandomSound()))
            await ctx.send(random.randint(1, 100))
        else:
            await ctx.send(random.randint(1, 100))
    except discord.ext.commands.CommandInvokeError:
        await ctx.send(random.randint(1, 100))
    except AttributeError:
        await ctx.send(random.randint(1, 100))
    except IndexError:
        await ctx.send(random.randint(1, 100))


@R5.command('join', brief="Joins R5 to the voice channel. * means voice only!")
async def join(ctx):
    vc = ctx.message.author.voice.channel
    try:
        await vc.connect()
        voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(snd.returnChannelSound()))
    except discord.ClientException:
        voice = discord.utils.get(R5.voice_clients, guild=ctx.guild)
        await ctx.send("BEEEEP!")
        voice.play(discord.FFmpegPCMAudio(RES_DIR + err))


@R5.command('leave', brief="*Kicks R5 from the voice channel.")
async def leave(ctx):
    try:
        R5.voice_clients[0].stop()
        R5.voice_clients[0].play(discord.FFmpegPCMAudio(snd.returnChannelSound()))
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
            R5.voice_clients[0].play(discord.FFmpegPCMAudio(snd.returnRandomSound()))
            await ctx.message.author.send("https://starwars.fandom.com/wiki/" + userquery)
        else:
            await ctx.message.author.send("https://starwars.fandom.com/wiki/" + userquery)
    except discord.ext.commands.CommandInvokeError:
        await ctx.message.author.send("https://starwars.fandom.com/wiki/" + userquery)
    except AttributeError:
        await ctx.message.author.send("https://starwars.fandom.com/wiki/" + userquery)


@R5.command('atmos', brief='*Plays atmospheric sounds. R5:help atmos to get list of sounds',
            description="List of sound options will be here")
async def atmos(ctx, arg: str):
    try:
        R5.voice_clients[0].play(discord.FFmpegPCMAudio(snd.returnAtmosphericSound(arg)))
    except IndexError:
        await ctx.send('BEEEEEP!')

@R5.command('resources', brief='Provides a list of player resources')
async def query(ctx):
    try:
        if not R5.voice_clients[0].is_playing():
            R5.voice_clients[0].play(discord.FFmpegPCMAudio(snd.returnRandomSound()))
            await ctx.message.author.send(fullResource)
        else:
            await ctx.message.author.send(fullResource)
    except discord.ext.commands.CommandInvokeError:
        await ctx.message.author.send(fullResource)
    except AttributeError:
        await ctx.message.author.send(fullResource)
    except IndexError:
        await ctx.message.author.send(fullResource)
    

R5.run("")
