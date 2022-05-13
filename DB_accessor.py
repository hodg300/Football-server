import os.path as op
from pprint import pprint as pp

from PlayersDB.CSV_handler import CSVHandler

class DBAccessor:

    def __init__(self):
        csv_file =  op.join(op.dirname(op.realpath(__file__)),"PlayersDB","Players.csv")
        self.db = CSVHandler(csv_file)

    def delete_player(self, player_name: str) -> bool:
        return self.db.delete_item(player_name)

    def add_player(self, player_data: dict) -> None:
        return self.db.add_item(player_data)

    def get_players_data(self):
        return self.db.json_data


if __name__ == "__main__":
    db = DBAccessor()
    pp(db.get_player_data('Nir'))