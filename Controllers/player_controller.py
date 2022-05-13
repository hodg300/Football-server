import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from


def delete_player(name):  # noqa: E501
    """Delete player&#x27;s Data

     # noqa: E501

    :param name: The name of the player
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_players():  # noqa: E501
    """Get all players

     # noqa: E501


    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'


def get_player_by_name(name):  # noqa: E501
    """Get Player by name

     # noqa: E501

    :param name: The name of the player
    :type name: str

    :rtype: Player
    """
    return 'do some magic!'


def player_post(body):  # noqa: E501
    """Add Player to DB

     # noqa: E501

    :param body: Add player to the players DataBase
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Player.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
