from abc import ABC, abstractmethod

class BaseHandlerInterface(ABC):

    def __init__(self):
        self._json_data = {}

    @property
    def json_data(self) -> dict:
        """Gets json data of players.
        :return: players data
        :rtype: json
        """
        return self._json_data

    @abstractmethod
    def update_json_data(self) -> None:
        """

        :param key: key of data to remove
        :return: if item was deleted successfully
        """
        pass

    @abstractmethod
    def delete_item(self, key: str = None) -> bool:
        """

        :param key: key of data to remove
        :return: if item was deleted successfully
        """
        pass

    @abstractmethod
    def add_item(self, item: list = None) -> None:
        """

        :param item: item to add as list
        :return: Added
        """
        pass
