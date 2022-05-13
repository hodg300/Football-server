# coding: utf-8


class Player:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, real_rating: float=None, grade_this_week: float=None, position: str=None, is_member: bool=None):  # noqa: E501
        """Player - a model defined in Swagger

        :param name: The name of this Player.  # noqa: E501
        :type name: str
        :param real_rating: The real_rating of this Player.  # noqa: E501
        :type real_rating: float
        :param grade_this_week: The grade_this_week of this Player.  # noqa: E501
        :type grade_this_week: float
        :param position: The position of this Player.  # noqa: E501
        :type position: str
        :param is_member: The is_member of this Player.  # noqa: E501
        :type is_member: bool
        """
        self.swagger_types = {
            'name': str,
            'real_rating': float,
            'grade_this_week': float,
            'position': str,
            'is_member': bool
        }

        self.attribute_map = {
            'name': 'name',
            'real_rating': 'realRating',
            'grade_this_week': 'gradeThisWeek',
            'position': 'position',
            'is_member': 'isMember'
        }
        self._name = name
        self._real_rating = real_rating
        self._grade_this_week = grade_this_week
        self._position = position
        self._is_member = is_member

    @property
    def name(self) -> str:
        """Gets the name of this Player.


        :return: The name of this Player.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Player.


        :param name: The name of this Player.
        :type name: str
        """

        self._name = name

    @property
    def real_rating(self) -> float:
        """Gets the real_rating of this Player.


        :return: The real_rating of this Player.
        :rtype: float
        """
        return self._real_rating

    @real_rating.setter
    def real_rating(self, real_rating: float):
        """Sets the real_rating of this Player.


        :param real_rating: The real_rating of this Player.
        :type real_rating: float
        """

        self._real_rating = real_rating

    @property
    def grade_this_week(self) -> float:
        """Gets the grade_this_week of this Player.


        :return: The grade_this_week of this Player.
        :rtype: float
        """
        return self._grade_this_week

    @grade_this_week.setter
    def grade_this_week(self, grade_this_week: float):
        """Sets the grade_this_week of this Player.


        :param grade_this_week: The grade_this_week of this Player.
        :type grade_this_week: float
        """

        self._grade_this_week = grade_this_week

    @property
    def position(self) -> str:
        """Gets the position of this Player.


        :return: The position of this Player.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position: str):
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

        self._position = position

    @property
    def is_member(self) -> bool:
        """Gets the is_member of this Player.


        :return: The is_member of this Player.
        :rtype: bool
        """
        return self._is_member

    @is_member.setter
    def is_member(self, is_member: bool):
        """Sets the is_member of this Player.


        :param is_member: The is_member of this Player.
        :type is_member: bool
        """

        self._is_member = is_member
