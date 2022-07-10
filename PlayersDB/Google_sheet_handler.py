import json
import os
import pprint
from PlayersDB.base_handler import BaseHandlerInterface
import os.path as op
from pprint import pp
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# define the scope

SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

class GoogleSheetHandler(BaseHandlerInterface):

    def __init__(self):
        super().__init__()

        # add credentials to the account
        credentialsPath = op.join(op.dirname(__file__), '.env')
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentialsPath, SCOPE)
        # authorize the clientsheet
        self.client = gspread.authorize(creds)

        self.__update_json_data()

    def __update_json_data(self):
        sheet = self.client.open('MondayFootball')
        sheet_instance = sheet.get_worksheet(0)
        records_data = sheet_instance.get_all_records()
        data = {}

        # Convert each row into a dictionary
        # and add it to data
        for row in records_data:
            # Assuming a column named 'No' to
            # be the primary key
            key = row['Name']
            data[key] = row

        # Open a json writer, and use the json.dumps()
        # function to dump data
        self._json_data = json.loads(json.dumps(data, indent=4))

    def delete_item(self, key : str=None) -> bool:
        pass

    def add_item(self, item : list=None) ->  None:
        sheet = self.client.open('MondayFootball')
        sheet_instance = sheet.get_worksheet(0)
        sheet_instance.insert_rows(item)


if __name__ == "__main__":
    gSheetHandler = GoogleSheetHandler()