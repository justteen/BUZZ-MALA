
 
# brought to you here(DARK VENOM) by... @Royal_King7..
# Don't remove these lines else Gey...

# _______________________________________________________________________________________________________________


from userbot import bot, CMD_HELP
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.utils import admin_cmd
import html
from telethon import events
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.events import ChatAction

async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`itu tidak mungkin tanpa ID pengguna`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Error... Please report di @ossuport", str(err))           
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

@borg.on(admin_cmd(pattern="gban ?(.*)"))
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("Gbanning pengguna ini !")
    else:
        dark = await dc.edit("Sedang diproses.....")
    me = await userbot.client.get_me()
    await dark.edit(f"Mencoba untuk ban secara keseluruhan..tunggu dan lihatlah.. dasar nob")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await dark.edit(f"**ada sesuatu yang salah ????**")
    if user:
        if user.id == 1457097205:
            return await dark.edit(
                f"**HELLOWW! Mana bisa aku ban pembuatku wlee..**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(f"**Banned Keseluruhan ???????? Total chat terkena **: `{a}`")
            except:
                b += 1
    else:
        await dark.edit(f"**Reply ke pengguna weii !!**")
    try:
        if gmute(user.id) is False:
            return await dark.edit(f"**Error! User telah gbanned.**")
    except:
        pass
    return await dark.edit(
        f"**Globally banned orang ini [{user.first_name}](tg://user?id={user.id}) terkena chat???? : {a} **"
    )


@borg.on(admin_cmd(pattern="ungben ?(.*)"))
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`tunggu, biarkan aku ungban orang cakep ini ????`")
    else:
        dark = await dc.edit("tunggu dan lihatlah! ")
    me = await userbot.client.get_me()
    await dark.edit(f"Mencoba untuk Ungban User !")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await dark.edit("ada sesuatu yang salah ????")
    if user:
        if user.id == 1457097205:
            return await dark.edit("**kamu tidak bisa gban atau ungban my boss... !**")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit(f"**Ungbaning orang cakep ini.. TERKENA CHAT - {a} **")
            except:
                b += 1
    else:
        await dark.edit("**Reply ke pengguna, sayangku...**")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**Error! User telah ungbanned.**")
    except:
        pass
    return await dark.edit(
        f"**Ungbanned orang cakep ini..memberikan dia kesempatan... ; Dia - [{user.first_name}](tg://user?id={user.id}) CHATS : {a} **"
    )




@borg.on(ChatAction)
async def handler(rkG): 
   if rkG.user_joined or rkG.user_added:      
       try:       	
         from userbot.modules.sql_helper.gmute_sql import is_gmuted
         guser = await rkG.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await rkG.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(rkG.chat_id, guser.id, view_messages=False)                              
                    await rkG.reply(
                     f"**Gbanned User(Manusia goodlooking ini) Gabung ke chat!!** \n"                      
                     f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**Action **  : `Banned orang kece ini lagi...Sed`")                                                
                 except:       
                    rkG.reply("`Tidak ada akses Ban.. @admins tolong ban dia. Dia adalah pengguna yang dilarang secara global dan berpotensi menjadi spammer.....!`")                   
                    return 
