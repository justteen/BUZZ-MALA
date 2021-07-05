import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME , CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events , errors , custom
import io
from platform import python_version , uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None :
    ALIVE_PIC = "https://telegra.ph/file/11e94d49e5fd5407be4ff.png" # we will change this later

DEFAULTUSER = str ( ALIVE_NAME ) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
ALIVE_MESSAGE = "**😜 MALA Bangun! MALA Bangun! xixixi 😜\n\n\n**"
ALIVE_MESSAGE += f"'Aku datang membawa kebahagiaan'"
ALIVE_MESSAGE += "`Status Bot \n\n\n`"
ALIVE_MESSAGE += f"`Kernel: Monolithic(linux) \n\n`"
ALIVE_MESSAGE += f"`Versi Kernel: 2.2.9  \n\n`"
ALIVE_MESSAGE += f"`MALA (MR.VICKS)  \n\n`"
ALIVE_MESSAGE += "`Default User Interface: KDE BUZZ \n\n`"
ALIVE_MESSAGE += f"`Support Channel` : @supbuz\n\n"
ALIVE_MESSAGE += f"'My Boss':{DEFAULTUSER} \n\n"
if ALIVE_MESSAGE is None :
    ALIVE_MESSAGE = "**😜 MALA Bangun! MALA Bangun! xixixi 😜\n\n\n**"
    ALIVE_MESSAGE += f"'Aku datang membawa kebahagiaan'"
    ALIVE_MESSAGE += f"`Support Channel` : @supbuz \n\n"
    ALIVE_MESSAGE += f"`ᎷᎽ ᏰᏫᏕᏕ`: {DEFAULTUSER} \n\n "


# @command(outgoing=True, pattern="^.awake$")
@borg.on ( admin_cmd ( pattern=r"awake" ) )
async def amireallyalive ( awake ) :
    """ For .awake command, check if the bot is running.  """
    await awake.delete ()
    await borg.send_file ( awake.chat_id , ALIVE_PIC , caption=ALIVE_MESSAGE )
