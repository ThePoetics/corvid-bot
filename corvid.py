# corvid.py
# A play on "the raven", this bot responds to a select list of commands from Twitch chat
#
# Future plans:  put a timeout on commands so they can only be used every [seconds]
#                add a list of literary quotes
#                add a followers command
#                test the bot somehow

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
  await ws.send_privmsg(os.environ['CHANNEL'], f"/me is ready for action")   # can change msg

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

# A command which triggers a random quote from Legend of Zelda
@raven.command(name='link')
async def link(ctx):
  link=['"Skyyaaaaaa!" -Link',
        '"Hyup, heep, hyeaaap!" -Link',
        '"Hey, listen!" -Navi',
        '"It\'s dangerous to go alone." -Old Man'
        '"Am I so beautiful that you\'ve no words left?" -Midna',
        '"It\'s a secret to everybody." -Moblin',
        '"HUP!" -Link',
        '"Heyaaaaaa!" -Link',
        '"Courage need not be remembered, for it is never forgotten" -Zelda',
        '"The wind, it is blowing." -Ganondorf',
        '"Open your eyes." -Zelda',
        '"The flow of time is always cruel." -Sheik',
        '"Master, your batteries are depleted." -Fi',
        '"Aaaaaaaaaaaaaaa!" -Link'
       ]
  await ctx.send(random.choice(link))

# A command which provides links to my (non-existent) socials
@raven.command(name='socials')
async def soc(ctx):
  soc="Poetics isn't on any social media but you can find his work at poeticsonline.net"
  await ctx.send(soc)

# A mod-only command which shouts out another streamer
@raven.command(name='so')
async def so(ctx: commands.Context, streamer: twitchio.PartialChatter):
  if (ctx.author.is_mod):
    so="A literary shout-out to our friend @{streamer}, give them a follow at twitch.tv/{streamer}"
    await ctx.send(so)

# A command which triggers a random fact about birds
@raven.command(name='birdfact')
async def link(ctx):
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

# A command which triggers a random fact about space
@raven.command(name='spacefact')
async def link(ctx):
  space=["The colors shown in images of the Cosmic Microwave Background differ in temperature by less than a millionth of a degree",
         "Enceladus, one of Saturn's moons, is so icy that it reflects 90% of the sun's light",
         "A sideral day is roughly 23.5 hours long, due to the orbit of the Earth around the Sun",
         "If Poetics went back to school today, he'd want to be an astro-climatologist",
         "Uranus is tilted more than 90 degrees, due to a massive impact in the past",
         "Neptune's moon Triton is the only known moon that orbits in retrograde",
         "Light from the Sun takes 8 minutes to reach Earth, but thousands of years for that energy to escape from the Sun in the first place",
         "Due to international treaties, the boundry for 'outer space' is 62 miles (100km) above sea-level",
         "Every planet in the solar system could fit between the Earth and Moon",
         "The Oort Cloud, from whence it is thought most comets originate, extends 3 light years in all directions",
         "The planet Saturn is so light it could float in water",
         "Astronauts can't burp in space due to microgravity; they are physically unable to",
         "Chinese astronomers first documented the appearance of Halley's Comet in BCE 240",
         "Black holes will slowly evaporate due to Hawking Radiation",
         "One teaspoon of a neutron star weighs as much as every human put together",
         "Space itself is expanding due to Dark Energy, with distant objects receding faster and faster",
         "Venus spins opposite every other planet, and its day is longer than its year"
         "The Sun accounts for more than 99.8% of the mass of our solar system",
         "There are about ten atoms per cubic meter of 'empty' space in the interstellar medium",
         "All atoms heavier than hydrogen were formed in the cores of stars; we are all made of star-stuff"
       ]
  await ctx.send(random.choice(space))

#=========================#
# End of command triggers #
#=========================#


# Final check
if __name__ == "__main__":
    raven.run()
