#!/usr/bin/env python

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def upload_file(file, folder_id, creders, sorted_files):
    """
    Uploads the csv created into a google sheets
    Arguments:
        file {str} -- name of file + path
        folder_id {str} -- folder id
        creders{str} -- path to creds.json
        sorted_files {str} -- name of file to upload
    RETURNS: uploaded or file already exists
    """
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive',
             'https://www.googleapis.com/auth/drive.appdata',
             'https://www.googleapis.com/auth/drive.file',
             'https://www.googleapis.com/auth/drive.metadata',
             'https://www.googleapis.com/auth/drive.metadata.readonly',
             'https://www.googleapis.com/auth/drive.photos.readonly',
             'https://www.googleapis.com/auth/drive.readonly']

    creds = ServiceAccountCredentials.from_json_keyfile_name(creders, scope)
    API = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': sorted_files,
        'description': 'This is a config document',
        'mimeType': 'text/plain',
        'parents': [folder_id]
    }
    media = MediaFileUpload(file, mimetype='text/plain', resumable=True)
    API.files().create(body=file_metadata, media_body=media, supportsTeamDrives=True, fields='id').execute()


"""
 if checkDest(API, sorted_files, folder_id):
     print('ERROR: File of the same name already exits')
 else:
     API.files().create(body=file_metadata, media_body=media, supportsTeamDrives=True, fields='id').execute()
     print('uploaded')
 """


def main():
    f = 'file path'
    fID = 'folder ID'
    creds = 'cred path'
    sortedFiles = 'file'
    upload_file(f, fID, creds, sortedFiles)


if __name__ == "__main__":
    main()
