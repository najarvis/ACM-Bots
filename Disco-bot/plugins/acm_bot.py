from disco.bot import Plugin
from tinydb import TinyDB, Query

db = TinyDB('db.json')

class ACMPlugin(Plugin):

    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('Pong!')

    @Plugin.command('award', '<name:str> <num:int>', grouop='points')
    def on_award_command(self, event, name, num):
        db.insert()
