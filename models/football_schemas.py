class Player:
    def __init__(self):
        """
        name = Player name
        real level = player rating
        match level = rating in the team
        role = Attack/Midfield/Defence
        GK = when he will be GK
        isMember = does this member bought a membership
        is_arrive = does this player comes this week
        """
        self.name = ""
        self.real_level = 2.5
        self.match_level = 3
        self.role = ""
        self.gk = 1
        self.is_member = False
        self.is_arrive = False


class Team:
    """
    Defence = has defencive member in the team
    Attack = has attacker member in the team
    players = list of players in the team
    team_level = team total score
    """
    def __init__(self):
        self.defence = False
        self.offence = False
        self.players = []
        self.team_level = 0

