from PlayersDB.CSV_handler import CSVHandler

class DBAccessor:

    def __init__(self):
        self.db = CSVHandler()
        self.data = CSVHandler.get_json()

    def delete_player(self, player_name: str) -> bool:
        return self.db.delete_item(player_name)

    def add_player(self, player_data: list) -> None:
        return self.db.add_item(player_data)

    def get_player(self, player_name: str) -> dict:

