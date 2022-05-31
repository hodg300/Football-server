# coding: utf-8


class Player:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, ranking: float=None, position: str=None, is_member: bool=None):  # noqa: E501
        """Player - a model defined in Swagger

        :param name: The name of this Player.  # noqa: E501
        :type name: str
        :param ranking: The real_rating of this Player.  # noqa: E501
        :type ranking: float
        :param gradeThisWeek: The grade_this_week of this Player.  # noqa: E501
        :type gradeThisWeek: float
        :param position: The position of this Player.  # noqa: E501
        :type position: str
        :param isMember: The is_member of this Player.  # noqa: E501
        :type isMember: bool
        """
        self.name = name
        self.ranking = ranking
        self.gradeThisWeek = 0
        self.goalkeeper = 0
        self.position = position
        self.isMember = is_member

    @property
    def Name(self) -> str:
        """Gets the name of this Player.


        :return: The name of this Player.
        :rtype: str
        """
        return self.name

    @Name.setter
    def Name(self, p_name: str):
        """Sets the name of this Player.


        :param name: The name of this Player.
        :type name: str
        """

        self.name = p_name

    @property
    def Ranking(self) -> float:
        """Gets the ranking of this Player.


        :return: The ranking of this Player.
        :rtype: float
        """
        return float(self.ranking)

    @Ranking.setter
    def Ranking(self, ranking: float):
        """Sets the ranking of this Player.


        :param ranking: The ranking of this Player.
        :type ranking: float
        """

        self.ranking = float(ranking)

    @property
    def GradeThisWeek(self) -> int:
        """Gets the grade_this_week of this Player.


        :return: The grade_this_week of this Player.
        :rtype: float
        """
        return self.gradeThisWeek

    @GradeThisWeek.setter
    def GradeThisWeek(self, grade_this_week: int):
        """Sets the grade_this_week of this Player.


        :param grade_this_week: The grade_this_week of this Player.
        :type grade_this_week: float
        """

        self.gradeThisWeek = grade_this_week

    @property
    def Goalkeeper(self) -> int:
        """Gets the grade_this_week of this Player.


        :return: The grade_this_week of this Player.
        :rtype: float
        """
        return self.goalkeeper

    @Goalkeeper.setter
    def Goalkeeper(self, goalkeeper: int):
        """Sets the grade_this_week of this Player.


        :param grade_this_week: The grade_this_week of this Player.
        :type grade_this_week: float
        """

        self.goalkeeper = goalkeeper

    @property
    def Position(self) -> str:
        """Gets the position of this Player.


        :return: The position of this Player.
        :rtype: str
        """
        return self.position

    @Position.setter
    def Position(self, position: str):
        """Sets the position of this Player.


        :param position: The position of this Player.
        :type position: str
        """
        allowed_values = ["Attack", "Midfield", "Defence"]  # noqa: E501
        if position not in allowed_values:
            raise ValueError(
                "Invalid value for `position` ({0}), must be one of {1}"
                .format(position, allowed_values)
            )

        self.position = position

    @property
    def IsMember(self) -> bool:
        """Gets the is_member of this Player.


        :return: The is_member of this Player.
        :rtype: bool
        """
        return self.isMember

    @IsMember.setter
    def IsMember(self, is_member: bool):
        """Sets the is_member of this Player.


        :param is_member: The is_member of this Player.
        :type is_member: bool
        """

        self.isMember = is_member
