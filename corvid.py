# corvid.py
# A play on "the raven", this bot responds to a select list of commands from Twitch chat
#
# Future plans: put a timeout on commands so they can only be used every [seconds]

import os
from twitchio.ext import commands
import time   # to prevent commands from being spammed

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
  print(f"{os.environ['BOT_NICK']} is online!")   # prints to stdout
  ws = raven._ws   # needed within event_ready
  await ws.send_privmsg(os.environ['CHANNEL'], f"/me is ready for action")   # can change msg

# Scans incoming chat every time a message is received
@raven.event
async def event_message(ctx):
  await raven.handle_commands(ctx)
  # Ignores itself and myself
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
        '"Courage need not be remembered, for it is never forgotten" -Zelda',
        '"The wind, it is blowing." -Ganondorf',
        '"Open your eyes." -Zelda',
        '"The flow of time is always cruel." -Sheik'
       ]
  await ctx.send('')

#=========================#
# End of command triggers #
#=========================#


# Final check
if __name__ == "__main__":
    raven.run()
