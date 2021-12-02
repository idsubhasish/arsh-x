import os

def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command

class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand('START_BOT', 'start')
        self.MirrorCommand = getCommand('MIRROR_BOT', 'mirror')
        self.UnzipMirrorCommand = getCommand('UNZIP_BOT', 'unzipmirror')
        self.ZipMirrorCommand = getCommand('ZIP_BOT', 'zipmirror')
        self.CancelMirror = getCommand('CANCEL_BOT', 'cancel')
        self.CancelAllCommand = getCommand('CANCEL_ALL_BOT', 'cancelall')
        self.ListCommand = getCommand('LIST_BOT', 'list')
        self.ListsearchCommand = getCommand('SEARCH_BOT',' search')
        self.SearchCommand = getCommand('TS_BOT', 'ts')
        self.StatusCommand = getCommand('STATUS_BOT', 'status')
        self.AuthorizedUsersCommand =  getCommand('USERS_BOT', 'users')
        self.AuthorizeCommand =  getCommand('AUTH_BOT', 'authorize')
        self.UnAuthorizeCommand = getCommand('UNAUTH_BOT','unauthorize')
        self.AddSudoCommand = getCommand('ADDSUDO_BOT', 'addsudo')
        self.RmSudoCommand = getCommand('RMSUDO_BOT', 'rmsudo')
        self.PingCommand =  getCommand('PING_BOT','ping')
        self.RestartCommand =  getCommand('RESTART_BOT', 'restart')
        self.StatsCommand = getCommand('STATS_BOT', 'stats')
        self.HelpCommand = getCommand('HELP_BOT', 'help')
        self.LogCommand = getCommand('LOG_BOT' , 'log')
        self.SpeedCommand = getCommand('SPEEDTEST_BOT', 'speedtest')
        self.CloneCommand = getCommand('CLONE_BOT', 'clone')
        self.CountCommand = getCommand('COUNT_BOT', 'count')
        self.WatchCommand = getCommand('WATCH_BOT', 'watch')
        self.ZipWatchCommand = getCommand('ZIPWATCH_BOT', 'zipwatch')
        self.QbMirrorCommand = getCommand('QBMIRROR_BOT', 'qbmirror')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIP_BOT', 'qbunzipmirror')
        self.QbZipMirrorCommand = getCommand('QBZIP_BOT', 'qbzipmirror')
        self.DeleteCommand = getCommand('DEL_BOT', 'del')
        self.ShellCommand = getCommand('SHELL_BOT', 'shell')
        self.ExecHelpCommand = getCommand('EXEHELP_BOT', 'exechelp')
        self.LeechSetCommand = getCommand('LEECHSET_BOT', 'leechset')
        self.SetThumbCommand = getCommand('SETTHUMB_BOT', 'setthumb')
        self.LeechCommand = getCommand('LEECH_BOT', 'leech')
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_BOT', 'unzipleech')
        self.ZipLeechCommand = getCommand('ZIPLEECH_BOT', 'zipleech')
        self.QbLeechCommand = getCommand('QBLEECH_BOT', 'qbleech')
        self.QbUnzipLeechCommand = getCommand('QBUNZIPLEECH_BOT', 'qbunzipleech')
        self.QbZipLeechCommand = getCommand('QBZIPLEECH_BOT', 'qbzipleech')
        self.LeechWatchCommand = getCommand('LEECHWATCH_BOT', 'leechwatch')
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_BOT', 'leechzipwatch')

BotCommands = _BotCommands()
