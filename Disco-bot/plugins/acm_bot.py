from disco.bot import Plugin
from tinydb import TinyDB, Query

db = TinyDB('db.json')

class ACMPlugin(Plugin):

    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('Pong!')

    @Plugin.command('award', '<name:str> <num:int>', group='points')
    def on_award_command(self, event, name, num):
        event.msg.reply("Awarding {} points to {}".format(name, num))
        points = db.table('points')
        User = Query()
        document = points.get(User.name == name)
        if document is not None:
            points.update({'points': document.points + num})
        else:
            points.insert({'name': name, 'points': num})

    @Plugin.command('list', group='points')
    def on_list_points_command(self, event):
        points = db.table('points')
        event.msg.reply("Point Listing:")
        for document in points.all():
            event.msg.reply("\t{}: {}".format(document['name'], document['points']))
