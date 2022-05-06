import math
import random
import csv
import json
import pprint
from copy import deepcopy

PLAYERS = []
COLORS = ['RED', 'BLUE', 'GREEN']
MAX_DIFF_BETWEEN_EQUAL_TEAMS = 0.5
MAX_DIFF_BETWEEN_NOT_EQUAL_TEAMS = 0.5


class Player:
    def __init__(self):
        self.name = ""
        self.real_level = 2.5
        self.match_level = 2.5
        self.role = ""
        self.gk = 1


class Team:
    def __init__(self):
        self.defence = False
        self.offence = False
        self.players = []
        self.team_level = 0


class Football:
    def __init__(self, path):
        self.players_levels = {}
        self.teams = {}
        self.path_to_file = path

    def clear(self):
        for team in self.teams:
            del team
        self.create_teams()

    def create_teams(self):
        teams_size = 3
        if len(PLAYERS) < 18:
            teams_size = 2

        for i in range(1, teams_size + 1):
            self.teams[str(i)] = Team()

    def read_CSV(self, file):
        players_file = open(file, "r", encoding="utf8")
        read = csv.reader(players_file)
        for row in read:
            if row[3].lower() == "v":
                p = Player()
                p.name = row[0]
                p.real_level = float(row[1])
                p.role = row[2]
                PLAYERS.append(p)
        PLAYERS.sort(key=self.sort_by_level, reverse=True)
        self.create_teams()
        i = 0
        for p in PLAYERS:
            p.match_level = int(i / len(self.teams)) + 1
            if p.match_level not in self.players_levels.keys():
                self.players_levels[p.match_level] = []
            self.players_levels[p.match_level].append(p)
            i += 1

    def sort_by_level(self, player):
        return player.real_level

    def print_player(self, p, color):
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
        print(big_team)
        return big_team

    def get_min_value_team(self):
        min_level = self.teams["1"].team_level
        min_team = "1"
        for name, team in self.teams.items():
            if team.team_level < min_level:
                min_level = team.team_level
                min_team = name
        return min_team

    def get_all_players_in_level(self, level):
        # in case there is no level 7 because team is only 6
        if level not in self.players_levels.keys():
            return []
        level_list = self.players_levels[level]
        shuffle_list = [i for i in level_list]
        random.shuffle(shuffle_list)
        # return level_list
        return shuffle_list

    def create_gorups(self):
        for i in range(1, int(len(PLAYERS) / len(self.teams)) + 1):
            players_list = self.get_all_players_in_level(i)
            for player in players_list:
                team = self.get_min_value_team()
                self.teams[team].team_level += float(player.real_level)
                self.teams[team].players.append(player)

    def validate_teams(self):
        scores = []
        players = []
        for name, team in self.teams.items():
            scores.append(team.team_level)
            players.append(len(team.players))
            for p in team.players:
                if p.role == "Defence":
                    team.defence = True
                if p.role == "Attack":
                    team.offence = True
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

    def teams_to_JSON(self):
        return json.dumps(self.teams, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


if __name__ == "__main__":
    path = "D:\\Data\\users\\omer-t\\Desktop\\PlayersEnglish.csv"
    f = Football(path)
    f.read_CSV(f.path_to_file)
    f.create_gorups()
    retry = 0

    while not f.validate_teams() and retry != 100:
        f.clear()
        f.create_gorups()
        retry += 1
    f.create_GK()
    f.print_teams_full()
    f.who_play_first()
    print("======================================")

    jsonTeams = f.teams_to_JSON()
    print(jsonTeams)
