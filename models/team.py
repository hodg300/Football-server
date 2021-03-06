# coding: utf-8

class Team:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """Team - a model defined in Swagger

        :param team_level: The team_level of this Team.  # noqa: E501
        :type team_level: float
        :param players: The players of this Team.  # noqa: E501
        :type players: List[object]
        """
        self.team_level = 0
        self.players = []
        self.defence = False
        self.attack = False

    @property
    def Team_level(self) -> float:
        """Gets the team_level of this Team.
        :return: The team_level of this Team.
        :rtype: float
        """
        return self.team_level

    @Team_level.setter
    def Team_level(self, team_level: float):
        """Sets the team_level of this Team.
        :param team_level: The team_level of this Team.
        :type team_level: float
        """

        self.team_level = team_level

    @property
    def Players(self) -> list[object]:
        """Gets the players of this Team.
        :return: The players of this Team.
        :rtype: List[object]
        """

        return self.players

    @Players.setter
    def Players(self, players: list[object]):
        """Sets the players of this Team.
        :param players: The players of this Team.
        :type players: List[object]
        """

        self.players = players

    @property
    def Defence(self) -> bool:
        """
        :return: if the team has defencing players
        :rtype: bool
        """

        return self.defence

    @Defence.setter
    def Defence(self, defence: bool):
        """
        :param defence: if the team has defencing players
        :type defence: bool
        """

        self.defence = defence

    @property
    def Attack(self) -> bool:
        """
        :return: if the team has attacking players
        :rtype: bool
        """

        return self.attack

    @Attack.setter
    def Attack(self, attack: bool):
        """
        :param attack: if the team has attacking players
        :type attack: bool
        """

        self.attack = attack
