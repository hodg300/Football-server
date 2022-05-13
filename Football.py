import math
import os.path
import random
import csv
import json
import pprint
from copy import deepcopy
from FootballSchemas import *
import os.path as path

COLORS = ['RED', 'BLUE', 'GREEN']
MAX_DIFF_BETWEEN_EQUAL_TEAMS = 0.5
MAX_DIFF_BETWEEN_NOT_EQUAL_TEAMS = 0.5

class Football:
    def __init__(self, file=path.join(path.curdir,'PlayersDB','Players.csv')):
        self.teams = {}
        self.db_path = file
        self.weekly_players = []
        self.all_players = []
        self.players_levels = {}

    def clear(self):
        for team in self.teams:
            del team
        self.teams = {}

    def create_teams(self):
        teams_size = 3
        if len(self.weekly_players) < 18:
            teams_size = 2
        for i in range(1, teams_size + 1):
            self.teams[str(i)] = Team()

    def generate_weekly_players(self):
        test_file = path.join(path.curdir, 'PlayersDB', 'test.csv')
        players_file = open(test_file, "r", encoding="utf8")
        read = csv.reader(players_file)
        next(read, None)
        for row in read:
            name = row[0]
            for p in self.all_players:
                player_name = p.name.replace(" ", "").lower()
                name = name.replace(" ", "").lower()
                if name == player_name:
                    self.weekly_players.append(p)

    def fillWeeklyPlayers(self, weekly_players:list):
        if not weekly_players:
            self.generate_weekly_players()
        else:
            i = 0
            for wp in weekly_players:
                for p in self.all_players:
                    player_name = p.name.replace(" ", "").lower()
                    name = wp.replace(" ", "").lower()
                    if name == p.name:
                        self.weekly_players.append(p)
        self.weekly_players.sort(key=self.sort_by_level, reverse=True)

    def read_CSV(self):
        players_file = open(self.db_path, "r", encoding="utf8")
        read = csv.reader(players_file)
        next(read, None)
        for row in read:
            p = Player()
            p.name = row[0]
            p.real_level = float(row[1])
            p.role = row[2]
            if row[3].lower() == "v":
                p.is_member = True
            self.all_players.append(p)
        self.all_players.sort(key=self.sort_by_level, reverse=True)

    def setMatchLevel(self):
        i = 0
        self.players_levels = {}
        for p in self.weekly_players:
            p.match_level = int(i / len(self.teams)) + 1
            if p.match_level not in self.players_levels.keys():
                self.players_levels[p.match_level] = []
            self.players_levels[p.match_level].append(p)
            i += 2

    def sort_by_level(self, player):
        return player.real_level

    def print_player(self, p, color='BLUE'):
        t = "Player [%s] in role [%s] with level [%s] will be goalkeeper number: [%d]" % (
        p.name, p.role, p.real_level, p.gk)
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

    def get_biggest_team(self):
        pprint.pprint(self.teams)
        big_team = len(self.teams["1"].players)
        for name, team in self.teams.items():
            if len(team.players) > big_team:
                big_team = len(team.players)
        return big_team

    def get_min_value_team(self):
        min_level = self.teams["1"].team_level
        min_team = "1"
        for name, team in self.teams.items():
            if team.team_level < min_level:
                min_level = team.team_level
                min_team = name
        return min_team

    def get_players_in_level(self, level):
        # in case there is no level 7 because team is only 6
        if level not in self.players_levels.keys():
            return []
        level_list = self.players_levels[level]
        shuffle_list = [i for i in level_list]
        random.shuffle(shuffle_list)
        # return level_list
        return shuffle_list

    def create_gorups(self):
        self.clear()
        self.create_teams()
        self.setMatchLevel()
        for i in range(1, int(len(self.weekly_players) / len(self.teams)) + 1):
            players_list = self.get_players_in_level(i)
            for player in players_list:
                team = self.get_min_value_team()
                self.teams[team].team_level += float(player.real_level)
                self.teams[team].players.append(player)
                if player.role.lower() == "defence":
                    self.teams[team].defence = True
                if player.role.lower() == "attack":
                    self.teams[team].offence = True

    def validate_teams(self):
        scores = []
        players = []
        for name, team in self.teams.items():
            scores.append(team.team_level)
            players.append(len(team.players))
            if not (team.offence and team.defence):
                print("Need at least 1 offence and 1 defence player. try again.")
                return False

        players.sort()
        print("players:", players)
        if players[len(players) - 1] - players[0] > 1:
            print("Different number of players in each team. try again.")
            return False
        scores.sort()
        print("scores:", scores)
        diff = MAX_DIFF_BETWEEN_EQUAL_TEAMS
        if players[len(players) - 1] != players[0]:
            diff = MAX_DIFF_BETWEEN_NOT_EQUAL_TEAMS
        if scores[len(scores) - 1] - scores[0] > diff:
            print("Gap between teams are too big. try again.")
            return False
        return True

    def who_play_first(self):
        first = random.choice(list(self.teams.keys()))
        second = random.choice(list(self.teams.keys()))
        while first == second:
            second = random.choice(list(self.teams.keys()))
        print("First match Will be [Team %s] Vs. [Team %s]! Good luck." % (first, second))

    def create_GK(self):
        for name, team in self.teams.items():
            newteam = deepcopy(team)
            random.shuffle(newteam.players)
            for gk in range(len(newteam.players)):
                for p in team.players:
                    if p.name == newteam.players[gk].name:
                        p.gk = gk + 1
                        break

    def print_teams_full(self):
        print("=============================== Monday Footbal =============================")
        color = 0
        for name, team in self.teams.items():
            t = "TEAM [%s] total level is: [%2f] and the players are:" % (name, team.team_level)
            self.print_color(t, COLORS[color])
            for p in team.players:
                self.print_player(p, COLORS[color])
            color += 1
            print("-------------------------------------------------------------- \n")

    def print_teams_half(self):
        print("=============================== Monday Footbal =============================")
        for name, team in self.teams.items():
            print("TEAM [%s] total level is: [%s] and the players are:" % (name, team.team_level))
            for p in team.players:
                print(p.name)
            print("-------------------------------------------------------------- \n")

    def teams_to_JSON(self):
        return json.dumps(self.teams, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


if __name__ == "__main__":
    f = Football()
    f.read_CSV()
    f.fillWeeklyPlayers([])
    f.create_gorups()
    retry = 0

    while not f.validate_teams() and retry != 100:
        f.create_gorups()
        retry += 1

    f.create_GK()
    f.print_teams_full()
    f.who_play_first()

    # print("======================================")
    # jsonTeams = f.teams_to_JSON()
    # print(jsonTeams)
    # print("======================================")

