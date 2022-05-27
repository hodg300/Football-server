import random
import os
import csv
import json
import pprint
from Controllers.players_controller import PlayerController
from Controllers.teams_controller import TeamsController
import os.path as path

COLORS = ['RED', 'BLUE', 'GREEN']
MAX_DIFF_BETWEEN_EQUAL_TEAMS = 0.5
MAX_DIFF_BETWEEN_NOT_EQUAL_TEAMS = 0.5


class FootballManager:
    def __init__(self):
        self.player_con = PlayerController()
        self.teams_con = TeamsController(self.player_con)
        self.player_con.load_players()

    def who_play_first(self):
        first = random.choice(list(self.teams_con.teams.keys()))
        second = random.choice(list(self.teams_con.teams.keys()))
        while first == second:
            second = random.choice(list(self.teams_con.teams.keys()))
        print("First match Will be [Team %s] Vs. [Team %s]! Good luck." % (first, second))

    def get_all_players(self):
        return self.player_con.get_all_players()

    def delete_player(self, name):
        return self.player_con.delete_player(name)

    def get_player_by_name(self, name):
        return self.player_con.get_player_by_name(name)

    def add_player(self, player):
        return self.player_con.add_player(player)

    def get_teams(self, players: dict) -> dict:
        """

        :param players: players to shuffle
        :return: json of 3 teams
        """
        weekly_players = json.loads(players)
        self.player_con.fillWeeklyPlayers(weekly_players.values())
        self.teams_con.create_gorups()
        retry = 0
        while not self.teams_con.validate_teams() and retry < 100:
            self.teams_con.create_gorups()
            retry += 1
        return json.loads(json.dumps(self.teams_con.teams, default=lambda o: o.__dict__,sort_keys=True, indent=4))

###########################################################################################################

def get_list_for_test(file):
    """
    Test
    :param file: file to test
    :return: testing
    """
    test_list = []
    test_file = open(file, "r")
    read = csv.reader(test_file)
    for row in read:
        name = row[0]
        test_list.append(name)
    return test_list

if __name__ == "__main__":
    f = FootballManager()
    test_list = get_list_for_test(path.join(os.getcwd(), "test", "weekly.csv"))
    json_data = f.get_teams(test_list)
    #pprint.pprint(json_data)
    f.teams_con.print_teams_full()
    f.who_play_first()

