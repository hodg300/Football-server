import json
import random


from models.player import Player
from DB_accessor import DBAccessor

COLORS = ['RED', 'BLUE', 'GREEN']

class PlayerController:

    def __init__(self):
        self.db_accessor = DBAccessor()
        self.weekly_players = []
        self.all_players = []
        self.players_levels = {}
        self.load_players()

    def clear(self):
        for player in self.all_players:
            del player
        self.all_players = []

    def load_players(self):
        self.clear()
        for player in self.db_accessor.db.json_data.values():
            name = player['Name']
            ranking = player['Ranking']
            position = player['Position']
            member = player['Member']
            p = Player(name, ranking, position, member)
            self.all_players.append(p)
        self.all_players.sort(key=lambda x: x.ranking, reverse=True)

    def fillWeeklyPlayers(self, weekly_players:list = []):
        i = 0
        for wp_name in weekly_players:
            for p in self.all_players:
                if wp_name == p.name:
                    self.weekly_players.append(p)
        self.weekly_players.sort(key=lambda x: x.ranking, reverse=True)

    def get_players_in_level(self, level):
        # in case there is no level 7 because team is only 6
        if level not in self.players_levels.keys():
            return []
        level_list = self.players_levels[level]
        shuffle_list = [i for i in level_list]
        random.shuffle(shuffle_list)
        return shuffle_list

    def delete_player(self, name) -> bool:
        success = self.db_accessor.delete_player(name)
        if success:
            self.load_players()
        return success

    def get_all_players(self):  # noqa: E501
        players_db = {}
        for player in self.db_accessor.db.json_data.values:
            players_db['name'] = player['name']
            players_db['isMember'] = player['Member']
        return json.loads(json.dumps(players_db, indent=4))


    def get_player_by_name(self, name):
        """Get Player by name
        :param name: The name of the player
        :type name: str
        :rtype: Player
        """
        return self.db_accessor.db.json_data[name]


    def player_post(self, player):
        """Add Player to DB
        :param body: Add player to the players DataBase
        :type body: dict | bytes
        :rtype: None
        """
        name = player['Name']
        ranking = player['Ranking']
        position = player['Position']
        member = player['Member']
        p = Player(name, ranking, position, member)
        self.all_players.append(p)
        self.db_accessor.add_player(player)
        return

    def print_player(self, p, color='BLUE'):
        t = "Player [%s] in position [%s] with level [%s] will be goalkeeper number: [%d]" % (
        p.name, p.position, p.ranking, p.goalkeeper)
        self.print_color(t, color)

    def print_color(self, t, color):
        if color == 'RED':
            print('\033[31m' + t + '\033[0m')
        elif color == 'BLUE':
            print('\033[36m' + t + '\033[0m')
        elif color == 'GREEN':
            print('\033[32m' + t + '\033[0m')
        else:
            print(t)