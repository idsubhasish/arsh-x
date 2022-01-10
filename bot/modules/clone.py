import random
import string
import threading
from telegram.ext import CommandHandler
from telegram import InlineKeyboardMarkup, ParseMode, InlineKeyboardButton
from bot.helper.mirror_utils.upload_utils import gdriveTools
from bot.helper.telegram_helper.message_utils import *
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.mirror_utils.status_utils.clone_status import CloneStatus
from bot import dispatcher, LOGGER, CLONE_LIMIT, STOP_DUPLICATE, download_dict, download_dict_lock, Interval, MIRROR_LOGS, BOT_PM, CHANNEL_USERNAME
from bot.helper.ext_utils.bot_utils import get_readable_file_size, is_gdrive_link, is_gdtot_link, new_thread
from bot.helper.mirror_utils.download_utils.direct_link_generator import gdtot
from bot.helper.ext_utils.exceptions import DirectDownloadLinkException

@new_thread
def cloneNode(update, context):
    if BOT_PM:
        try:
            msg1 = f'Added your Requested link to clone\n'
            send = bot.sendMessage(update.message.from_user.id, text=msg1,)
            send.delete()
        except Exception as e:
            LOGGER.warning(e)
            bot_d = bot.get_me()
            b_uname = bot_d.username
            uname = f'<a href="tg://user?id={update.message.from_user.id}">{update.message.from_user.first_name}</a>'
            channel = CHANNEL_USERNAME
            botstart = f"http://t.me/{b_uname}"
            keyboard = [
                [InlineKeyboardButton("Click Here to Start Me", url=f"{botstart}")],
                [InlineKeyboardButton("Join our Updates Channel", url=f"t.me/{channel}")]]
            message = sendMarkup(
                f"Dear {uname},\n\n<b>I found that you haven't started me in PM (Private Chat) yet.</b>\n\nFrom now on i will give link and leeched files in PM and log channel only.",
                bot, update, reply_markup=InlineKeyboardMarkup(keyboard))
            threading.Thread(target=auto_delete_message, args=(bot, update.message, message)).start()
            return
    args = update.message.text.split(" ", maxsplit=1)
    reply_to = update.message.reply_to_message
    if len(args) > 1:
        link = args[1]
        if update.message.from_user.username:
            tag = f"@{update.message.from_user.username}"
        else:
            tag = update.message.from_user.mention_html(update.message.from_user.first_name)
    elif reply_to is not None:
        link = reply_to.text
        if reply_to.from_user.username:
            tag = f"@{reply_to.from_user.username}"
        else:
            tag = reply_to.from_user.mention_html(reply_to.from_user.first_name)
    else:
        link = ''
    gdtot_link = is_gdtot_link(link)
    if gdtot_link:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", context.bot, update)
            link = gdtot(link)
            deleteMessage(context.bot, msg)
        except DirectDownloadLinkException as e:
            deleteMessage(context.bot, msg)
            return sendMessage(str(e), context.bot, update)
    if is_gdrive_link(link):
        gd = gdriveTools.GoogleDriveHelper()
        res, size, name, files = gd.helper(link)
        if res != "":
            return sendMessage(res, context.bot, update)
        if STOP_DUPLICATE:
            LOGGER.info('Checking File/Folder if already in Drive...')
            smsg, button = gd.drive_list(name, True, True)
            if smsg:
                msg3 = "File/Folder is already available in Drive.\nHere are the search results:"
                sendMarkup(msg3, context.bot, update, button)
                if gdtot_link:
                    gd.deletefile(link)
                return
        if CLONE_LIMIT is not None:
            LOGGER.info('Checking File/Folder Size...')
            if size > CLONE_LIMIT * 1024**3:
                msg2 = f'Failed, Clone limit is {CLONE_LIMIT}GB.\nYour File/Folder size is {get_readable_file_size(size)}.'
                return sendMessage(msg2, context.bot, update)
        if files <= 10:
            msg = sendMessage(f"Cloning: <code>{link}</code>", context.bot, update)
            result, button = gd.clone(link)
            deleteMessage(context.bot, msg)
        else:
            drive = gdriveTools.GoogleDriveHelper(name)
            gid = ''.join(random.SystemRandom().choices(string.ascii_letters + string.digits, k=12))
            clone_status = CloneStatus(drive, size, update, gid)
            with download_dict_lock:
                download_dict[update.message.message_id] = clone_status
            sendStatusMessage(update, context.bot)
            result, button = drive.clone(link)
            with download_dict_lock:
                del download_dict[update.message.message_id]
                count = len(download_dict)
            try:
                if count == 0:
                    Interval[0].cancel()
                    del Interval[0]
                    delete_all_messages()
                else:
                    update_all_messages()
            except IndexError:
                pass
        cc = f'\n\n<b>Cloned By: </b>{tag}'
        if button in ["cancelled", ""]:
            sendMessage(f"{tag} {result}", context.bot, update)
        else:
            sendMarkup(result + cc, context.bot, update, button)
        if gdtot_link:
            gd.deletefile(link)
        if MIRROR_LOGS:
            try:
                for i in MIRROR_LOGS:
                    msg1 = f'<b>File Cloned: </b> <code>{name}</code>\n\n'
                    msg1 += f'<b>Size: </b> {get_readable_file_size(size)}\n\n'
                    msg1 += f'<b>By: </b>{tag}\n\n'
                    bot.sendMessage(chat_id=i, text=msg1, reply_markup=button, parse_mode=ParseMode.HTML)
            except Exception as e:
                LOGGER.warning(e)
            if BOT_PM:
                try:
                    bot.sendMessage(update.message.from_user.id, text=msg1, reply_markup=button, parse_mode=ParseMode.HTML)
                except Exception as e:
                    LOGGER.warning(e)
                    return

    else:
        message = sendMessage('Send Gdrive or gdtot link along with command or by replying to the link by command', context.bot, update)
        threading.Thread(target=auto_delete_message, args=(bot, update.message, message)).start()
        return

clone_handler = CommandHandler(BotCommands.CloneCommand, cloneNode, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(clone_handler)
