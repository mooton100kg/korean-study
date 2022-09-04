from operator import index
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('jsonfile/alert-brook-361418-d95992f17aaf.json', scope)

# authorize the clientsheet 
# client = gspread.authorize(creds)

# sheet = client.open('Korean')
# sheet_instance = sheet.get_worksheet(0)

def getData():
    # records_data = sheet_instance.get_all_records()
    # records_df = pd.DataFrame.from_dict(records_data).sort_values(by=['correct_flashcard'])
    # flashcard_data = records_df.to_dict(orient='list')
    # records_df = pd.DataFrame.from_dict(records_data).sort_values(by=['correct_spelling'])
    # spelling_data = records_df.to_dict(orient='list')
    
    return "hello"

# def update_data(word, correct, type):
#     cell = sheet_instance.find(word)

#     if type == "flashcard":
#         col = 3
#     elif type == "spelling":
#         col = 4

#     if correct:
#         x = int(sheet_instance.cell(cell.row, col).value) + 1
#     elif not correct:
#         x = int(sheet_instance.cell(cell.row, col).value) - 1
#     sheet_instance.update_cell(cell.row, col, x)

# def add_word(korean, thai):
#     sheet_instance.insert_row([korean, thai, 0, 0], index=2)
