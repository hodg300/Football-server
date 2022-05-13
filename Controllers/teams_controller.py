import connexion
import six
import json
from copy import deepcopy
import random
from models.team import Team
from models.player import Player
from DB_accessor import DBAccessor
from Controllers.players_controller import PlayerController

COLORS = ['RED', 'BLUE', 'GREEN']
MAX_DIFF_BETWEEN_EQUAL_TEAMS = 0.5
MAX_DIFF_BETWEEN_NOT_EQUAL_TEAMS = 0.5

class TeamsController:

    def __init__(self, pl_controller: PlayerController):

        self._teams = {}
        self.player_con = pl_controller

    @property
    def teams(self) -> dict:
        """
        :return: the teams
        :rtype: bool
        """

        return self._teams

    def clear(self):
        for team in self._teams:
            del team
        self._teams = {}

    def create_teams(self):
        teams_size = 3
        if len(self.player_con.weekly_players) < 18:
            teams_size = 2
        for i in range(1, teams_size + 1):
            self._teams[str(i)] = Team()

    def setMatchLevel(self):
        i = 0
        self.player_con.players_levels = {}
        for p in self.player_con.weekly_players:
            p.grade_this_week = int(i / len(self._teams)) + 1
            if p.grade_this_week not in self.player_con.players_levels.keys():
                self.player_con.players_levels[p.grade_this_week] = []
            self.player_con.players_levels[p.grade_this_week].append(p)
            i += 1

    def get_biggest_team(self):
        pprint.pprint(self._teams)
        big_team = len(self._teams["1"].players)
        for name, team in self._teams.items():
            if len(team.players) > big_team:
                big_team = len(team.players)
        return big_team

    def get_min_value_team(self):
        min_level = self._teams["1"].team_level
        min_team = "1"
        for name, team in self._teams.items():
            if team.team_level < min_level:
                min_level = team.team_level
                min_team = name
        return min_team

    def create_gorups(self):
        self.clear()
        self.create_teams()
        self.setMatchLevel()
        for i in range(1, int(len(self.player_con.weekly_players) / len(self._teams)) + 1):
            players_list = self.player_con.get_players_in_level(i)
            for player in players_list:
                team = self.get_min_value_team()
                self._teams[team].team_level += float(player.ranking)
                self._teams[team].players.append(player)
                if player.position.lower() == "defence":
                    self._teams[team].defence = True
                if player.position.lower() == "attack":
                    self._teams[team].attack = True
        self.create_GK()

    def validate_teams(self):
        scores = []
        players = []
        for name, team in self._teams.items():
            scores.append(team.team_level)
            players.append(len(team.players))
            if not (team.attack and team.defence):
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

    def create_GK(self):
        for name, team in self.teams.items():
            newteam = deepcopy(team)
            random.shuffle(newteam.players)
            for gk in range(len(newteam.players)):
                for p in team.players:
                    if p.name == newteam.players[gk].name:
                        p.goalkeeper = gk + 1
                        break

    def print_color(self, t, color):
        if color == 'RED':
            print('\033[31m' + t + '\033[0m')
        elif color == 'BLUE':
            print('\033[36m' + t + '\033[0m')
        elif color == 'GREEN':
            print('\033[32m' + t + '\033[0m')
        else:
            print(t)

    def print_teams_full(self):
        print("=============================== Monday Footbal =============================")
        color = 0
        for name, team in self._teams.items():
            t = "TEAM [%s] total level is: [%2f] and the players are:" % (name, team.team_level)
            self.print_color(t, COLORS[color])
            for p in team.players:
                self.player_con.print_player(p, COLORS[color])
            color += 1
            print("-------------------------------------------------------------- \n")

    def print_teams_half(self):
        print("=============================== Monday Footbal =============================")
        for name, team in self._teams.items():
            print("TEAM [%s] total level is: [%s] and the players are:" % (name, team.team_level))
            for p in team.players:
                print(p.name)
            print("-------------------------------------------------------------- \n")

    def teams_to_JSON(self):
        return json.dumps(self.teams, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)