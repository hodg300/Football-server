import os.path as op
from pprint import pprint as pp
# test
from PlayersDB.CSV_handler import CSVHandler
from PlayersDB.Google_sheet_handler import GoogleSheetHandler

class DBAccessor:

    def __init__(self):
        self.db = GoogleSheetHandler()

    def delete_player(self, player_name: str) -> bool:
        return self.db.delete_item(player_name)

    def add_player(self, player_data: list) -> None:
        return self.db.add_item(player_data)

    def get_players_data(self):
        return self.db.json_data

    def read_updated_data(self):
        return self.db.update_json_data()


if __name__ == "__main__":
    db = DBAccessor()
    pp(db.get_player_data('Nir'))