import json
import random


from models.player import Player
from DB_accessor import DBAccessor

COLORS = ['RED', 'BLUE', 'GREEN']
NUMBER_OF_PLAYERS = 21

class PlayerController:

    def __init__(self):
        self.db_accessor = DBAccessor()
        self.weekly_players = []
        self.all_players = []
        self.players_levels = {}

    def clear(self):
        for player in self.all_players:
            del player
        self.all_players = []
        self.__clear_weekly_players()

    def __clear_weekly_players(self):
        for player in self.weekly_players:
            del player
        self.weekly_players = []

    def load_players(self):
        self.clear()
        self.db_accessor.read_updated_data()
        for player in self.db_accessor.db.json_data.values():
            name = player['Name']
            ranking = player['Ranking']
            position = player['Position']
            is_member = player['Member'] == 'V'
            is_arrive = player['Arrive'] == 'V'
            p = Player(name, ranking, position, is_member, is_arrive)
            self.all_players.append(p)
        self.all_players.sort(key=lambda x: x.Ranking, reverse=True)

    def fillWeeklyPlayers(self, weekly_players:list = []):
        self.__clear_weekly_players()
        for wp_name in weekly_players:
            for p in self.all_players:
                if str(wp_name) == p.Name:
                    self.weekly_players.append(p)
        self.weekly_players.sort(key=lambda x: x.Ranking, reverse=True)
        if len(self.weekly_players) is not NUMBER_OF_PLAYERS:
            return False
        return True

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
            for p in self.all_players:
                if p.Name == name:
                    self.all_players.remove(p)
        return success

    def get_all_players(self):  # noqa: E501
        players_db = {}
        playerID = 1
        self.load_players()
        for p in self.all_players:
            players_db[playerID] = {}
            players_db[playerID]['name'] = p.Name
            players_db[playerID]['isArrive'] = p.IsArrive
            playerID += 1
        return json.loads(json.dumps(players_db, indent=4))

    def get_player_by_name(self, name):
        """Get Player by name
        :param name: The name of the player
        :type name: str
        :rtype: Player
        """
        for p in self.all_players:
            if p.Name == name:
                return json.loads(json.dumps(p, default=lambda o: o.__dict__, sort_keys=True, indent=4))
        return {}


    def add_player(self, player_json):
        """Add Player to DB
        :param body: Add player to the players DataBase
        :type body: dict | bytes
        :rtype: None
        """
        player = json.loads(player_json)
        try:
            name = player['name']
            ranking = player['ranking']
            position = player['position']
            member = player['isMember']
        except KeyError:
            return False
        new_player = Player(name, ranking, position, member)
        for p in self.all_players:
            if p.Name == new_player.Name:
                self.delete_player(name)
        self.all_players.append(new_player)
        self.db_accessor.add_player(list(player.values()))
        return True

    def change_to_dict(self, player):
        return json.dumps(player, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)



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