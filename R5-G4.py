import discord, discord.player, random, ffmpeg
import discord.player
from discord.ext import commands

print("Vwooooo!")

R5 = commands.Bot(command_prefix='$R5:')


@R5.command('obligation')
async def obligation(ctx):
    await ctx.channel.send(str(random.randint(1, 100)))


@R5.command('play')
async def play(ctx):
    print("Vwwooooo...")
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(R5.voice_clients, guild=guild)
    audio_source = discord.player.FFmpegPCMAudio('home/dennis/Documents/personal/repo/R5-G4/r2sounds.mp3')
    # audio_source = discord.FFmpegPCMAudio('home/dennis/Documents/personal/repo/R5-G4/r2sounds.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)


R5.run("")
