import asyncio, discord, random
from discord.ext import commands
import music_clips
#pip install --upgrade aiohttp

bot = commands.Bot(command_prefix = '!')
@bot.event
async def on_ready():
    print('Connected and ready to use!')

#bad-words.txt contains one blacklisted phrase per line
with open('bad_words.txt') as f:
    bad_words = [bad_word.strip().lower() for bad_word in f.readlines()]

@bot.event
async def on_message(message):
    message_content = message.content.strip().lower().split()
    #Automaticly blocking bad words
    bad_mes = 0
    for bad_word in bad_words:
        if bad_word in message_content:
            bad_mes = 1
    if bad_mes != 0:
        await bot.send_message(message.channel, f'{message.author.mention},' +
        ' your message has been censored.')
        await bot.delete_message(message)
    #Mod operation with 2 integer numbers
    if len(message_content) == 3 and message_content[1] == 'mod':
        try:
            value1 = int(message_content[0])
            value2 = int(message_content[2])
        except ValueError:
            pass
        if isinstance(value1, int) == True and isinstance(value2, int) == True:
            res = value1 % value2
            await bot.send_message(message.channel, res)

#!help_menu command will demonstrate how to work with a bot
@bot.command(pass_context = True)
async def help_menu(ctx):
    info = 'If you want to see a good(on my opinion) videoclip, type !music\n' +
    'I can motivate you to work, just type !motivation for it.\n' +
    'I can solve any examples in the form x % y and give you correct answer.'
    await bot.say(info)

#!music command gives random music clip
@bot.command(pass_context = True)
async def music(ctx):
    await bot.say(random.choice(music_clips.links_to_clips))

#!motivation command gives random useful advice
timeout = 100
@bot.command(pass_context = True)
async def motivation(ctx):
    phrases = [
    'Start working on your diploma!',
    'Leave DOTA and do something useful!',
    "It's time to warmup.",
    'Avoid Time-Wasting Habits',
    'Give yourself a stop time!',
    "I think it's time for you to become a BUG Bounty Hunter!",
    "Programmers fail all the time, don't be mad bro!",
    "Don't give up!",
    'Keep Calm and Keep On Coding'
    ]
    while(1):
        await bot.say(random.choice(phrases))
        await asyncio.sleep(timeout)

BOT-TOKEN = ''
bot.run(BOT-TOKEN)
