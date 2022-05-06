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

