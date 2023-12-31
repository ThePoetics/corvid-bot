# corvid.py
# A play on "the raven", this bot responds to a select list of commands from Twitch chat
#
# Future plans:  put a timeout on commands so they can only be used every [seconds]
#                add a list of literary quotes
#                add a followers command (for follower count)
#                test the bot somehow
#                split out the fact/list commands into other include files?

import os
from twitchio.ext import commands
import time   # to prevent commands from being spammed
import random

# This code traps errors and prevents them from logging to stdout ot stderr
class MyBot(commands.Bot):
  asynd def event_command_error(self, context: commands.Context, error: Exception):
        if isinstance(error, commands.CommandNotFound):
            return

        print(error)

raven = commands.Bot(
  # Initial variables, taken from .env
  # Use pipenv to run the bot to auto-load that file
  irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

# Runs once on bot initialization
@raven.event
async def event_ready():
  print(f"{os.environ['BOT_NICK']} is ready to write.")   # prints to stdout
  ws = raven._ws   # needed within event_ready
  await ws.send_privmsg(os.environ['CHANNEL'], f"/me is ready to write")   # can change msg

# Scans incoming chat every time a message is received
@raven.event
async def event_message(ctx):
  await raven.handle_commands(ctx)
  # Ignores itself
  if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
    return

#===============================#
# Here are the command triggers #
#===============================#

# !socials - a command which provides links to my (non-existent) socials
@raven.command(name='socials')
async def soc(ctx) -> None:
  soc="Poetics isn't on any social media but you can find his written works at poeticsonline.net"
  await ctx.send(soc)

# !support - a command to display a tip message and link to my Ko-Fi
@raven.command(name='support',aliases=('tip'))
async def support(ctx) -> None:
  support="Poetics is eternally grateful to all who support him and his storytelling. For those who want to say thank you monitarily, please visit https://ko-fi.com/U6U3CBPO to tip via Ko-Fi"
  await ctx.send(support)

# !who - a command which gives a little about me
@raven.command(name='who',aliases=('poet'))
async def who(ctx) -> None:
  who="Poetics (GamingPoet on Twitch) is an author and life-long storyteller, playing games in his spare time. He/Him pronouns"
  await ctx.send(who)

# !so - a mod-only command which shouts out another streamer
@raven.command(name='so',aliases=('shoutout'))
async def so(ctx: commands.Context, streamer: twitchio.PartialChatter) -> None:
  if (ctx.author.is_mod):
    so="A literary shout-out to our friend @{streamer}! Give them a follow at twitch.tv/{streamer}"
    await ctx.send(so)

## !firstraid - a command to commemorate the first raid I ever received
#@raven.command(name='firstraid')
#async def fr(ctx) -> None:
#  fr="A huge thanks to >><< who was this channel's first raid on >><< with >><< viewers!"
#  await ctx.send(fr)

## !firstsub - a command to commemorate the first sub I ever received
#@raven.command(name='firstsub')
#async def fs(ctx) -> None:
#  fs="A huge thanks to >><< who was this channel's first subscriber on >><<!"
#  await ctx.send(fs)

## !record - a command to celebrate the highest Hype Train
#@raven.command(name='hype')
#async def hype(ctx) -> None:
#  hype="Our biggest hype train ever was Level >><< on >><<!"
#  await ctx.send(hype)

# !back - announcing that someone has come back into chat
@raven.command(name='back',aliases=('wb'))
async def back(ctx) -> None:
  back="Let's all welcome {ctx.author.name} back to the writing room!"
  await ctx.send(back)

# !lurk - Random lurk messages posted to chat
@raven.command(name='lurk',aliases=('away'))
async def lurk(ctx) -> None:
  lurk=["{ctx.author.name} is away, lurking in the depths of literature and planning their next adventure",
        "{ctx.author.name} is off on a quest for inspiration",
        "{ctx.author.name} is seeking inspiration elsewhere for the time being",
        "Don't bother {ctx.author.name}, they're in deep thought about what to create next",
        "{ctx.author.name} sneaks off to read another chapter of a great book",
        "The clickety-clack from {ctx.author.name}'s keyboard shows they're busy creating new worlds",
        "{ctx.author.name} is taking a break from taking a break",
        "There once was a {ctx.author.name} from Nantucket ... no, no, that doesn't rhyme",
        "It's time for {ctx.author.name} to put their head down and dream of new possibilities for a while",
        "{ctx.author.name} is off to sharpen their wits for the coming battles",
        "Has anyone seen {ctx.author.name}? Their stuff is still here so they must be coming back",
        "{ctx.author.name} is drowning out the world by diving into imagination",
        "As the Bard once penned, \"Exit {ctx.author.name}, pursued by bear\""
       ]
  await ctx.send(random.choice(lurk))

# !birdfact - A command which triggers a random fact about birds
@raven.command(name='birdfact')
async def bird(ctx) -> None:
  bird=["Peregrin falcons are the world's fastest animals, capable of dives over 200mph",
        "Owls can't move their eyes and so have to move their entire head",
        "The common starling can spend over 10 continuous months flying, without any breaks",
        "Hummingbirds are the only avian that can fly backwards",
        "Falconry was developed over 4000 years ago in eastern and central Asia",
        "Most birds' feathers weigh more than their hollow skeletons",
        "Emperor penguins can stay underwater for up to 18 minutes",
        "Birds are the only vertibrates with a fused collarbone",
        "The word 'parakeet' literally means 'long tail'",
        "Crows can remember human faces",
        "Sufferers of anatidaephobia fear that a goose or duck is somehow watching them",
        "Kestrels and falcons have the same power of sight as humans",
        "The word 'falcon' comes from the Latin 'falix', meaning a curved blade or sickle"
       ]
  await ctx.send(random.choice(bird))

# !spacefact - A command which triggers a random fact about space
@raven.command(name='spacefact')
async def space(ctx) -> None:
  space=["The colors shown in images of the Cosmic Microwave Background differ in temperature by less than a millionth of a degree",
         "Enceladus, one of Saturn's moons, is so icy that it reflects 90% of the sun's light",
         "A sideral day is roughly 23.5 hours long, due to the orbit of the Earth around the Sun",
         "If Poetics went back to school today, he'd want to be an exo-climatologist",
         "Uranus is tilted more than 90 degrees, due to a massive impact in the distant past",
         "Neptune's moon Triton is the only known moon that orbits in retrograde",
         "Light from the Sun takes 8 minutes to reach Earth, but thousands of years for that energy to escape from the Sun in the first place",
         "Due to international treaties, the boundry for 'outer space' is 62 miles (100km) above sea-level",
         "Every planet in our solar system, lined up, could fit between the Earth and Moon with room to spare",
         "The Oort Cloud, from whence it is thought most comets originate, extends 3 light years in all directions",
         "The planet Saturn is so light it could float in water",
         "In space, food doesn't make astronauts burp due to the way microgravity interacts with food",
         "Chinese astronomers first documented the appearance of Halley's Comet in BCE 240",
         "Black holes will slowly evaporate due to Hawking Radiation",
         "One teaspoon of a neutron star weighs as much as every human put together",
         "Space itself is expanding due to Dark Energy, with distant objects receding faster and faster",
         "Venus spins opposite every other planet, and its day is longer than its year"
         "The Sun accounts for more than 99.8% of the mass of our solar system",
         "There are about ten atoms per cubic meter of 'empty' space in the interstellar medium",
         "All atoms heavier than hydrogen were formed in the cores of stars; we are all made of star-stuff",
         "The Sun takes 240 million years to orbit the center of the Milky Way"
       ]
  await ctx.send(random.choice(space))

# !link - A command which triggers a random quote from Legend of Zelda
@raven.command(name='link',aliases=('zelda'))
async def link(ctx) -> None:
  link=['"Skyyaaaaaa!" -Link',
        '"Hyup, heep, hyeaaap!" -Link',
        '"Hey, listen!" -Navi',
        '"It\'s dangerous to go alone." -Old Man',
        '"Am I so beautiful that you\'ve no words left?" -Midna',
        '"It\'s a secret to everybody." -Moblin',
        '"HUP!" -Link',
        '"Heyaaaaaa!" -Link',
        '"Courage need not be remembered, for it is never forgotten" -Zelda',
        '"The wind, it is blowing." -Ganondorf',
        '"Open your eyes." -Zelda',
        '"The flow of time is always cruel." -Sheik',
        '"Master, your batteries are depleted." -Fi',
        '"Aaaaaaaaaaaaaaa!" -Link',
        '"Time passes, people move." -Sheik',
        '"Can Hyrule\'s destiny really depend on such a lazy boy?!" -Navi',
        '"Those who do not know the danger of wielding power will, before long, be ruled by it" -Lanayru',
        '"My mind is getting hazy" -Flute Kid',
        '"What makes you happy? I wonder... does it make others happy, too?" -Moon Child',
        'Your friends... do these people think of you as a friend?" -Moon Child',
        '"You\'ve met with a terrible fate, haven\'t you?" -Happy Mask Salesman',
        '"OOOOOOOOH, THANK YOU!" -Beedle',
        '"When all of this is over, will you come to wake me up?" -Zelda',
        '"Do you ever feel a strange sadness as dusk falls?" -Rusl',
        '"Would you like to hear that again?" -Kaepora Gaebora',
        '"We\'ll be friends forever. Won\'t we?" -Saria',
        '"Do you have any idea how that made me feel inside?" -Ghirahim',
        '"Kaaaaaaaay!" -Fishman',
        '"A sword has no strength unless the hand that wields it has courage." -Hero\'s Shade',
        '"May the light of blessing grant you the strength you seek." -Shrine Statues',
        '"I\'m sure an answer will come to you. Wisdom takes time." -Queen Sonia'
       ]
  await ctx.send(random.choice(link))

#=========================#
# End of command triggers #
#=========================#


# Final check
if __name__ == "__main__":
    raven.run()
