import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Használd az alábbi URL-t a hitelesítési adatokhoz
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# TODO: Replace 'your_credentials.json' with the path to your own credentials file.
credentials = ServiceAccountCredentials.from_json_keyfile_name('your_credentials.json', scope)


gc = gspread.authorize(credentials)

wks = gc.open("python google sheet").sheet1


list_of_lists = wks.get_all_values()
print(list_of_lists)

wks.update_acell('B2', 'Hello world!')
