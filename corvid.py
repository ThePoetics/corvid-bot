# corvid.py
# A play on "the raven", this bot responds to a select list of commands from Twitch chat

import os
from twitchio.ext import commands

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
@raven.command(name='link')
async def link(ctx):
  # Insert array here and randomize responses
  await ctx.send('')


# Final check
if __name__ == "__main__":
    raven.run()
