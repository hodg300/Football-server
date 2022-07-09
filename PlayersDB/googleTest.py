import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

sheet = client.open('MondayFootball')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

# get all the records of the data
records_data = sheet_instance.get_all_records()

records_df = pd.DataFrame.from_dict(records_data)

# view the top records
print(records_df.head())