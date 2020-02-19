#!/usr/bin/env python
from __future__ import print_function

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build


def upload_file(name, path, SPREADSHEET_ID, creders):
    """
    Uploads the csv created into a google sheets
    Arguments:
        name {str} -- name of file expected/created
        path {str} -- path to csv
        SPREADSHEET_ID {str} -- where to upload file before
        creders {str} -- path to google SA credentials json
    RETURNS: google API responce
    """
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(creders, scope)
    API = build('sheets', 'v4', credentials=creds)

    with open(path, 'r') as csv_file:
        csvContents = csv_file.read()

    worksheet_name = name
    add_tab_request = {"requests": {"addSheet": {"properties": {"title": worksheet_name}}}}
    request = API.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=add_tab_request)
    request.execute()
    sheet_id = find_sheet_id_by_name(worksheet_name, SPREADSHEET_ID, API=API)

    body = {
        'requests': [{
            'pasteData': {
                "coordinate": {
                    "sheetId": sheet_id,
                    "rowIndex": "0",
                    "columnIndex": "0",
                },
                "data": csvContents,
                "type": 'PASTE_NORMAL',
                "delimiter": ',',
            }
        }]

    }

    request1 = API.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body)
    response = request1.execute()
    return response

def find_sheet_id_by_name(sheet_name, SPREADSHEET_ID, API):
    """
    Uploads the csv created into a google sheets
    Arguments:
        sheet_name {str} -- the worksheet_ID
        SPREADSHEET_ID {str} -- where to upload file before
        API {str} -- session build from google API
    RETURNS: google sheet ID
    """
    sheets_with_properties = API.spreadsheets().get(spreadsheetId=SPREADSHEET_ID,
                                                    fields='sheets.properties').execute().get('sheets')
    for sheet in sheets_with_properties:
        if 'title' in sheet['properties'].keys():
            if sheet['properties']['title'] == sheet_name:
                return sheet['properties']['sheetId']

def main():

    name = 'name'
    path = 'path'
    spreadsheetID = 'ID'
    creds = 'creds'

    upload_file(name,path,spreadsheetID,creds)

if __name__ == "__main__":
    main()
