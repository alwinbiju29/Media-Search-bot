import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from info import START_MSG, CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, START_IMG
from utils import Media, get_file_details 
from pyrogram.errors import UserNotParticipant
logger = logging.getLogger(__name__)

ABOUT_TEXT = """
<b>᯽≫⋯⋯ʙᴏᴛ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ⋯⋯≪᯽</b>
<b>🎃 ꜰᴜʟʟ ɴᴀᴍᴇ : ʀᴀᴍᴀɴᴀɴ</b>
<b>🍒 ᴜꜱᴇʀ ɴᴀᴍᴇ : @ɪᴍ_ᴏᴅɪʏᴀɴ</b>

<b>🇮🇳 ᴄᴏᴜɴᴛʀʏ : ɪɴᴅɪᴀ</b>
<b>🪴 ꜱᴛᴀᴛᴇ : ᴋᴇʀᴀʟᴀ</b>
<b>🍂 ᴅɪꜱᴛʀɪᴄᴛ : ᴋᴏᴛᴛᴀʏᴀᴍ</b>

<b>{} സർ എന്ന പിന്നെ ഞാൻ അങ്ങോട്ട്</b>
"""

@Client.on_message(filters.command("start"))
async def start(bot, cmd):
    usr_cmdall1 = cmd.text
    if usr_cmdall1.startswith("/start subinps"):
        if AUTH_CHANNEL:
            invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
            try:
                user = await bot.get_chat_member(int(AUTH_CHANNEL), cmd.from_user.id)
                if user.status == "kicked":
                    await bot.send_message(
                        chat_id=cmd.from_user.id,
                        text="Sorry Sir, You are Banned to use me.",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                ident, file_id = cmd.text.split("_-_-_-_")
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="**Please Join My Updates Channel to use this Bot!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🍿 ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 🍿", url="https://t.me/joinchat/x6V1RmEmmGBhMjQ1")
                            ],
                            [
                                InlineKeyboardButton("🍁 Try Again 🍁", callback_data=f"checksub#{file_id}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="Something went Wrong.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        try:
            ident, file_id = cmd.text.split("_-_-_-_")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=files.file_size
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = f"{files.file_name}"
                buttons = [
                    [
                        InlineKeyboardButton("🍁ᴊᴏɪɴ ɢʀᴏᴜᴘ🍁", url="https://t.me/Movie_factorys"),
                        InlineKeyboardButton("💥ꜱʜᴀʀᴇ💥", url="https://t.me/share/url?url=**🤩%20മൂവി%20ഫാക്റ്ററി%20🤩%0A%0Aഏത്%20അർധരാത്രി%20ചോദിച്ചാലും%20പടം%20കിട്ടും,%20ലോകത്തിലെ%20ഒട്ടുമിക്ക%20ഭാഷകളിലുമുള്ള%20സിനിമകളുടെ%20കളക്ഷൻ..%20❤️%0A%0A👇%20GROUP%20LINK%20👇%0A@Movie_factorys%0A@Movie_factorys%0A@Movie_factorys**")
                    ],
                    [
                        InlineKeyboardButton("📝 ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴜʙᴛɪᴛɪʟᴇ 📝", url="https://t.me/subtitle_dl_bot")
                    ]
                    ]
                await bot.send_cached_media(
                    chat_id=cmd.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")
    elif len(cmd.command) > 1 and cmd.command[1] == 'subscribe':
        invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🍿 ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 🍿", url="https://t.me/joinchat/x6V1RmEmmGBhMjQ1")
                    ]
                ]
            )
        )
    else:
        await cmd.reply_photo(photo=START_IMG, caption=START_MSG.format(cmd.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤴 ʙᴏᴛ ᴏᴡɴᴇʀ 🤴", callback_data='about'),
                        InlineKeyboardButton("🍁 ʙᴏᴛ ɢʀᴏᴜᴘ 🍁", url="https://t.me/Movie_factorys")
                    ],
                    [
                        InlineKeyboardButton("💥 ꜱʜᴀʀᴇ 💥", url="https://t.me/share/url?url=**%F0%9F%A4%A9%20%E0%B4%AE%E0%B5%82%E0%B4%B5%E0%B4%BF%20%E0%B4%AB%E0%B4%BE%E0%B4%95%E0%B5%8D%E0%B4%B1%E0%B5%8D%E0%B4%B1%E0%B4%B1%E0%B4%BF%20%F0%9F%A4%A9%0A%0A%E0%B4%8F%E0%B4%A4%E0%B5%8D%20%E0%B4%85%E0%B5%BC%E0%B4%A7%E0%B4%B0%E0%B4%BE%E0%B4%A4%E0%B5%8D%E0%B4%B0%E0%B4%BF%20%E0%B4%9A%E0%B5%8B%E0%B4%A6%E0%B4%BF%E0%B4%9A%E0%B5%8D%E0%B4%9A%E0%B4%BE%E0%B4%B2%E0%B5%81%E0%B4%82%20%E0%B4%AA%E0%B4%9F%E0%B4%82%20%E0%B4%95%E0%B4%BF%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B5%81%E0%B4%82,%20%E0%B4%B2%E0%B5%8B%E0%B4%95%E0%B4%A4%E0%B5%8D%E0%B4%A4%E0%B4%BF%E0%B4%B2%E0%B5%86%20%E0%B4%92%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B5%81%E0%B4%AE%E0%B4%BF%E0%B4%95%E0%B5%8D%E0%B4%95%20%E0%B4%AD%E0%B4%BE%E0%B4%B7%E0%B4%95%E0%B4%B3%E0%B4%BF%E0%B4%B2%E0%B5%81%E0%B4%AE%E0%B5%81%E0%B4%B3%E0%B5%8D%E0%B4%B3%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%E0%B4%95%E0%B4%B3%E0%B5%81%E0%B4%9F%E0%B5%86%20%E0%B4%95%E0%B4%B3%E0%B4%95%E0%B5%8D%E0%B4%B7%E0%B5%BB..%20%E2%9D%A4%EF%B8%8F%0A%0A%F0%9F%91%87%20GROUP%20LINK%20%F0%9F%91%87%0A@Movie_factorys%0A@Movie_factorys%0A@Movie_factorys**"),
                        InlineKeyboardButton("🔐 ᴄʟᴏꜱᴇ 🔐", callback_data='close')
                    ],                    
                    [
                        InlineKeyboardButton("🍿 ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 🍿", url="https://t.me/joinchat/x6V1RmEmmGBhMjQ1")
                    ]
                ]
            )
        )
        
@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "about":
        await query.answer=ABOUT_TEXT.format(update.from_user.mention),
            show_alert=True
        )
    else:
        await update.message.delete()

@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')
@Client.on_message(filters.command('about'))
async def bot_info(bot, message):
    buttons = [
        [
            InlineKeyboardButton('🍿 ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 🍿', url='https://t.me/joinchat/x6V1RmEmmGBhMjQ1'),
            InlineKeyboardButton('🍁 ʙᴏᴛ ɢʀᴏᴜᴘ 🍁', url='https://t.me/Movie_factorys')
        ]
        ]
