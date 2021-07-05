# Made by BUZZ

import asyncio
import time
from datetime import datetime
from platform import python_version as ver

from telethon import __version__, events
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError

from userbot import ALIVE_NAME, CMD_HELP, Lastupdate
from userbot.utils import admin_cmd
from . import *

#### Variables ####
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Ṃ Λ Ɫ Λ"

ALIVE_MSG = Config.ALIVE_MSG
if ALIVE_MSG is None :
    ALIVE_MSG = f"Ini {DEFAULTUSER} BUZZ - ṂΛⱢΛ Userbot"

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None :
    ALIVE_PIC = "https://telegra.ph/file/11e94d49e5fd5407be4ff.png"

botversion = "0.1"

#### Functions ####
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@borg.on(admin_cmd(pattern=r"alive"))
async def alive(e):
    start = datetime.now()
    end = datetime.now()
    ping = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    cap = """
**Ṃ Λ Ɫ Λ usᥱrδ᧐ᴛ**
**{}**
❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅
╔════╣ ＩＮＦＯＭＡＳＩ ＢＯＴ ╠═❁⫸
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ **Ⲟⲱⲛⲉʀ** - `ᗷᑌƵƵ` 
║┣⪼ **Ⲋⲧⲁⲧυⲋ** - `Ⲟⲛⳑⲓⲛⲉ`
║┣⪼ **Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ** - `{}`
║┣⪼ **Ⳙⲣⲧⲓⲙⲉ** - `{}` 
║┣⪼ **Ⲃⲟⲧ Ⲣⲓⲛⳋ** - `{}
║┣⪼ **Ⲣⲩⲧⲏⲟⲛ** - `{}` 
║┣⪼ **Ⲧⲉⳑⲉⲧⲏⲟⲛ** - `{}` 
║┣⪼ [✨ ᗷᑌƵƵ - ṂΛⱢΛ 𐌵sᥱrδ᧐ᴛ✨](https://t.me\/psycho_syridwan
║╰━━━━━━━━━━━━━━━➣
╚════════════════════════════❁⫸
""".format(
        ALIVE_MSG,
        DEFAULTUSER,
        botversion,
        uptime,
        ping,
        ver(),
        __version__,
    )
    try:
        await e.get_chat() 
        await borg.send_file(e.chat_id, file=ALIVE_PIC)
        await borg.send_file(e.chat_id, cap, link_preview=False)
        await e.delete()
    except ChatSendMediaForbiddenError:
        await e.edit(cap, link_preview=False)

       
CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Cek kalau ᗷᑌƵƵ - MALA 𐌵sᥱrδ᧐ᴛ alive"
    }
)
