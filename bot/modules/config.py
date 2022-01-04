# Implement By https://github.com/arshsisodiya
# Based on this https://github.com/DevsExpo/FridayUserbot/blob/master/plugins/heroku_helpers.py

from pyrogram import filters, types, emoji
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.ext_utils.heroku_helper import get_text, check_heroku
from bot import *
# Add Variable

@app.on_message(filters.command('setvar') & filters.user(OWNER_ID))
@check_heroku
async def set_varr(client, message, app_):
    msg_ = await message.reply_text("`Please Wait!`")
    heroku_var = app_.config()
    _var = get_text(message)
    if not _var:
        await msg_.edit("`Here is Usage Syntax: /setvar KEY VALUE`", parse_mode="markdown")
        return
    if " " not in _var:
        await msg_.edit("`Variable VALUE needed !`", parse_mode="markdown")
        return
    var_ = _var.split(" ", 1)
    if len(var_) > 2:
        await msg_.edit("`Here is Usage Syntax: /setvar KEY VALUE`", parse_mode="markdown")
        return
    _varname, _varvalue = var_
    await msg_.edit(f"Variable `{_varname}` Added With Value `{_varvalue}!` Restarting now.....")
    heroku_var[_varname] = _varvalue

# Delete Variable
        
@app.on_message(filters.command('delvar') & filters.user(OWNER_ID))
@check_heroku
async def del_varr(client, message, app_):
    msg_ = await message.reply_text("`Please Wait!`", parse_mode="markdown")
    heroku_var = app_.config()
    _var = get_text(message)
    if not _var:
        await msg_.edit("`Give Var Name As Input!`", parse_mode="markdown")
        return
    if _var not in heroku_var:
        await msg_.edit("`This Var Doesn't Exists!`", parse_mode="markdown")
        return
    await msg_.edit(f"Sucessfully Deleted `{_var}` Var! Restarting now.....", parse_mode="markdown")
    del heroku_var[_var]

# CONFIG LIST #

__header__='📕 **Page** **{}**\n\n'

@app.on_message(filters.command(BotCommands.ConfigMenuCommand) & filters.user(OWNER_ID))
async def config_menu(_, message):
    await message.reply(
        f"**Hello {message.from_user.mention}**,\n\n**If you want to add or set Variable in Heroku use** `/setvar`\n\n**If you want to delete Variable in Heroku use `/delvar`**\n\n**WARNING! Very Recommended to do this command in private since it's contain Bot info.**\n\n**Here's This is Helios-Mirror Bot Current Configs**",
        reply_markup=types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(
                        f"{emoji.CROSS_MARK}", callback_data='docs_end'
                    ),
                    types.InlineKeyboardButton(
                        'BOT CONFIG', callback_data='docs_1'
                    ),
                ]
            ]
        ),
    )

@app.on_callback_query(filters.regex('^docs_') & filters.user(OWNER_ID))
async def config_button(_, query):
    data = query.data.split('_')[1]
    if data == '1':
        return await query.message.edit(
            __header__.format(data)
            + f"**[ IMPORTANT CONFIGS ]**\n\n`BOT_TOKEN`:\n`{BOT_TOKEN}`\n\n`TELEGRAM_API`: \n`{TELEGRAM_API}`\n\n`TELEGRAM_HASH`: \n`{TELEGRAM_HASH}`\n\n **`BASE_URL_OF_BOT`: \n`{BASE_URL}`\n\n **`DATABASE_URL`: \n`{DB_URI}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_17'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_2')
                    ]
                ]
            )
        )
    elif data == '2':
        return await query.message.edit(
            __header__.format(data)
            + f"**[ Drive and Index Config ]**\n\n`GDRIVE_FOLDER_ID`: \n`{parent_id}`\n\n`IS_TEAM_DRIVE`: \n`{IS_TEAM_DRIVE}`\n\n`USE_SERVICE_ACCOUNTS`: \n`{USE_SERVICE_ACCOUNTS}`"
              f"\n\n`INDEX_URL`: \n`{INDEX_URL}`\n\n`STOP_DUPLICATE`: \n`{STOP_DUPLICATE}`\n\n`GD_INFO`: \n`{GD_INFO}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_1'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_3')
                    ]
                ]
            )
        )
    elif data == '3':
        return await query.message.edit(
            __header__.format(data)
            + f"**[ Mega Config ]**\n\n`MEGA_API_KEY`: \n`{MEGA_API_KEY}`\n\n`MEGA_EMAIL_ID`: \n`{MEGA_EMAIL_ID}`\n\n`MEGA_PASSWORD`: \n`{MEGA_PASSWORD}`"
              f"\n\n[ Block Mega Config ]**\n\n`BLOCK_MEGA_FOLDER`: \n`{BLOCK_MEGA_FOLDER}`\n\n`BLOCK_MEGA_LINKS`: \n`{BLOCK_MEGA_LINKS}`\n\n",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_2'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_4')
                    ]
                ]
            )
        )
    elif data == '4':
        return await query.message.edit(
            __header__.format(data)
            + f"**[ Mirror Log Config ]**\n\n`LOGS_CHATS`: \n`{LOGS_CHATS}`\n\n[ Leech Dump Config ]**\n\n`LOG_CHANNEL`: \n`{LOG_CHANNEL}`\n\n",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_3'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_5')
                    ]
                ]
            )
        )
    elif data == '5':
        return await query.message.edit(
            __header__.format(data)
            + f"**[ Limit Size Config ]**\n\n`TORRENT_DIRECT_LIMIT`: `{TORRENT_DIRECT_LIMIT}` GB\n\n`ZIP_UNZIP_LIMIT`: `{ZIP_UNZIP_LIMIT}` GB"
              f"\n\n`CLONE_LIMIT`: `{CLONE_LIMIT}` GB\n\n`MEGA_LIMIT`: `{MEGA_LIMIT}` GB",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_4'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_6')
                    ]
                ]
            )
        )
    elif data == '6':
        return await query.message.edit(
            __header__.format(data)
            + f"**[ Leech Configs ]**\n\n`TG_SPLIT_SIZE`: `{TG_SPLIT_SIZE}` kb \n\n`AS_DOCUMENT`: `{AS_DOCUMENT}`"
              f"\n\n`EQUAL_SPLITS`: `{EQUAL_SPLITS}`\n\n`CUSTOM_FILENAME`: `{CUSTOM_FILENAME}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_5'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_7')
                    ]
                ]
            )
        )
    elif data == '7':
        return await query.message.edit(
            __header__.format(data)
            + f"**[ Telegraph UI ]**\n\n`AUTHOR_NAME`: \n`{AUTHOR_NAME}`\n\n`AUTHOR_URL`: \n`{AUTHOR_URL}`\n\n`TITLE_NAME`: \n`{TITLE_NAME}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_6'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_8')
                    ]
                ]
            )
        )

    elif data == '8':
        return await query.message.edit(
            __header__.format(data)
            + f"**[External Config URL]**\n\n`CONFIG_FILE_URL`: \n`{CONFIG_FILE_URL}` \n\n`ACCOUNTS_ZIP_URL`: \n`{ACCOUNTS_ZIP_URL}`"
              f"\n\n`TOKEN_PICKLE_URL`: \n`{TOKEN_PICKLE_URL}`\n\n`MULTI_SEARCH_URL`: \n`{MULTI_SEARCH_URL}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_7'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_9')
                    ]
                ]
            )
        )
    elif data == '9':
        return await query.message.edit(
            __header__.format(data)
            + f"**[GDTOT Cookies]**\n\n`PHPSESSID`: \n`{PHPSESSID}`\n\n`CRYPT`: \n`{CRYPT}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_8'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_10')
                    ]
                ]
            )
        )

    elif data == '10':
        user = sudo = ''
        user += '\n'.join(str(id) for id in AUTHORIZED_CHATS)
        sudo += '\n'.join(str(id) for id in SUDO_USERS)
        return await query.message.edit(
            __header__.format(data)
            + f"**[ User ID Config ]**\n\n`OWNER_ID`: \n`{OWNER_ID}`\n\n`AUTHORIZED_CHATS`: \n`{achats}`\n\n`SUDO_USERS`: \n`{schats}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_9'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_11')
                    ]
                ]
            )
        )
    elif data == '11':
        return await query.message.edit(
            __header__.format(data)
            + f"**[ Button Config ]**\n\n`BUTTON_FOUR_NAME`: \n`{BUTTON_FOUR_NAME}`\n\n`BUTTON_FOUR_URL`: \n`{BUTTON_FOUR_URL}`"
              f"\n\n`BUTTON_FIVE_NAME`: \n`{BUTTON_FIVE_NAME}`\n\n`BUTTON_FIVE_URL`: \n`{BUTTON_FIVE_URL}`\n\n`BUTTON_SIX_NAME`: \n`{BUTTON_SIX_NAME}`"
              f"\n\n`BUTTON_SIX_URL`: \n`{BUTTON_SIX_URL}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_10'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_12')
                    ]
                ]
            )
        )
    elif data == '12':
        return await query.message.edit(
            __header__.format(data)
            + f"**[ Heroku Config ]**\n\n **`HEROKU_APP_NAME`: \n`{HEROKU_APP_NAME}`\n\n **`HEROKU_API_KEY`: \n`{HEROKU_API_KEY}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_11'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_13')
                    ]
                ]
            )
        )
    elif data == '13':
        return await query.message.edit(
            __header__.format(data)
            + f" **[ Others Config ]**\n\n`VIEW_LINK`: \n`{VIEW_LINK}`\n\n`DOWNLOAD_STATUS_UPDATE_INTERVAL`: \n`{DOWNLOAD_STATUS_UPDATE_INTERVAL}` Seconds "
              f"\n\n`IGNORE_PENDING_REQUESTS`: \n`{IGNORE_PENDING_REQUESTS}` \n\n`AUTO_DELETE_MESSAGE_DURATION`: \n`{AUTO_DELETE_MESSAGE_DURATION}` Seconds "
              f"\n\nDOWNLOAD_DIR: \n`{DOWNLOAD_DIR}`\n\nDatabase Url: \n`{DB_URI}`\n\n[ Shortener Config ]**\n\n`SHORTENER`: \n`{SHORTENER}`"
              f"\n\n`SHORTENER_API`: \n`{SHORTENER_API}`\n\n`UPTOBOX_TOKEN`: \n`{UPTOBOX_TOKEN}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_12'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_14')
                    ]
                ]
            )
        )


    elif data == '14':
        return await query.message.edit(
            __header__.format(data)
            + f" **[ Qbittorrent Plugins ]**\n\n`SEARCH_PLUGINS`: \n`{SEARCH_PLUGINS}`\n\n`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_13'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_15')
                    ]
                ]
            )
        )


    #Code for Up Showing Commands

    elif data == '15':
        return await query.message.edit(
            __header__.format(data)
            + f" **[ BOT COMMANDS ]**\n\n`START_COMMAND`: `{BotCommands.StartCommand}`\n\n`MIRROR_COMMAND`: `{BotCommands.MirrorCommand}` \n\n`ZIP_COMMAND`: `{BotCommands.ZipMirrorCommand}` \n\n`UNZIP_COMMAND`: `{BotCommands.UnzipMirrorCommand}` "
              f"\n\n`CANCEL_COMMAND`: `{BotCommands.CancelMirror}` \n\n`LIST_COMMAND`: `{BotCommands.ListCommand}`\n\n`SEARCH_COMMAND`: `{BotCommands.SearchCommand}`\n\n`STATUS_COMMAND`: `{BotCommands.StatusCommand}` \n\n`STATS_COMMAND`: `{BotCommands.StatsCommand}`"
              f"\n\n`HELP_COMMAND`: `{BotCommands.HelpCommand}` \n\n`CLONE_COMMAND`: `{BotCommands.CloneCommand}`\n\n`COUNT_COMMAND`: `{BotCommands.CountCommand}`\n\n`WATCH_COMMAND`: `{BotCommands.WatchCommand}` \n\n`ZIPWATCH_COMMAND`: `{BotCommands.ZipWatchCommand}` "
              f"\n\n`ZIPWATCH_COMMAND`: `{BotCommands.ZipWatchCommand}` \n\n`QBMIRROR_COMMAND`: `{BotCommands.QbMirrorCommand}` \n\n`QBZIP_COMMAND`: `{BotCommands.QbZipMirrorCommand}` \n\n`QBUNZIP_COMMAND`: `{BotCommands.QbUnzipMirrorCommand}` \n\n`TOR_COMMAND`: `{BotCommands.TorrentSearchCommand}`",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_14'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_16')
                    ]
                ]
            )
        )

    elif data == '16':
        return await query.message.edit(
            __header__.format(data)
            + f" **[ LEECH COMMANDS ]**\n\n`LEECH_COMMAND`: `{BotCommands.ListCommand}` \n\n`LEECHSET_COMMAND`: `{BotCommands.LeechSetCommand}` \n\n`SETTHUMB_COMMAND`: `{BotCommands.SetThumbCommand}` \n\n`UNZIPLEECH_COMMAND`: `{BotCommands.UnzipLeechCommand}` "
              f"\n\n`ZIPLEECH_COMMAND`: `{BotCommands.ZipLeechCommand}` \n\n`QBLEECH_COMMAND`: `{BotCommands.QbLeechCommand}` \n\n`QBUNZIPLEECH_COMMAND`: `{BotCommands.QbUnzipLeechCommand}` "
              f"\n\n`QBZIPLEECH_COMMAND`: `{BotCommands.QbZipLeechCommand}`\n\n`LEECHWATCH_COMMAND`: `{BotCommands.LeechWatchCommand}` \n\n`LEECHZIPWATCH_COMMAND`: `{BotCommands.LeechZipWatchCommand}` ",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_15'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_17')
                    ]
                ]
            )
        )
    elif data == '17':
        return await query.message.edit(
            __header__.format(data)
            + f" **[ SUDO COMMANDS ]**\n\n`AUTH_COMMAND`: `{BotCommands.AuthorizeCommand}` \n\n`UNAUTH_COMMAND`: `{BotCommands.UnAuthorizeCommand}`\n\n`ADDSUDO_COMMAND`: `{BotCommands.AddSudoCommand}` \n\n`RMSUDO_COMMAND`: `{BotCommands.RmSudoCommand}` \n\n`LOG_COMMAND`: `{BotCommands.LogCommand}` "
              f"\n\n`RESTART_COMMAND`: `{BotCommands.RestartCommand}` \n\n`SPEED_COMMAND`: `{BotCommands.SpeedCommand}`"
              f"\n\n`DELETE_COMMAND`: `{BotCommands.DeleteCommand}` \n\n`SHELL_COMMAND`: `{BotCommands.ShellCommand}` \n\n`CONFIG_COMMAND`: `{BotCommands.ConfigMenuCommand}` \n\n`CANCEL_ALL_COMMAND`: `{BotCommands.CancelAllCommand}` ",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(f"{emoji.LEFT_ARROW}", callback_data='docs_16'),
                        types.InlineKeyboardButton(f"{emoji.CROSS_MARK}", callback_data='docs_end'),
                        types.InlineKeyboardButton(f"{emoji.RIGHT_ARROW}", callback_data='docs_1')
                    ]
                ]
            )
        )

    elif data == 'end':
        return await query.message.delete()
