import random
import os
import csv
import json
import pprint
from copy import deepcopy
from Controllers.players_controller import PlayerController
from Controllers.teams_controller import TeamsController
import os.path as path

COLORS = ['RED', 'BLUE', 'GREEN']
MAX_DIFF_BETWEEN_EQUAL_TEAMS = 0.5
MAX_DIFF_BETWEEN_NOT_EQUAL_TEAMS = 0.5

class Football:
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

    def create_GK(self):
        for name, team in self.teams_con.teams.items():
            newteam = deepcopy(team)
            random.shuffle(newteam.players)
            for gk in range(len(newteam.players)):
                for p in team.players:
                    if p.name == newteam.players[gk].name:
                        p.goalkeeper = gk + 1
                        break

def get_list_for_test(file):
    test_list = []
    test_file = open(file, "r")
    read = csv.reader(test_file)
    for row in read:
        name = row[0]
        test_list.append(name)
    return test_list

if __name__ == "__main__":
    f = Football()
    test_list = get_list_for_test(path.join(os.getcwd(), "test", "weekly.csv"))
    f.player_con.fillWeeklyPlayers(test_list)
    f.teams_con.create_gorups()
    retry = 0

    while not f.teams_con.validate_teams() and retry != 100:
        f.teams_con.create_gorups()
        retry += 1

    f.create_GK()
    f.teams_con.print_teams_full()
    f.who_play_first()
