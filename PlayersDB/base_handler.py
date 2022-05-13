
class BaseHandlerInterface:

    def create_database(self) -> None:
        """

        :return: data baser creation
        """
    pass

    def get_json(self) -> dict:
        """Gets json data of the players.
        :return: players data
        :rtype: json
        """
        pass

    def delete_item(self, key: str = None) -> bool:
        """

        :param key: key of data to remove
        :return: if item was deleted seccesfully
        """
        pass

    def add_item(self, item: list = None) -> None:
        """

        :param item: item to add as list
        :return: Added
        """
        pass